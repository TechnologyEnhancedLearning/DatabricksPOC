import pytest
import getpass
import os
from pyspark.sql import functions as F
from datetime import datetime, timedelta



@pytest.fixture(scope="module")
def bronze_ods_schema(spark):
    """Build schema name once for this test module"""

    catalog = os.getenv("CATALOG")
    schema_prefix = os.getenv("SCHEMA_PREFIX")
    print (f"catalog {catalog} prefix {schema_prefix}")

    return f"{catalog}.{schema_prefix}bronze_ods"

@pytest.fixture(scope="module")
def contact_details_table(spark, bronze_ods_schema):
    """Load contact_details table once for this test module"""
    return spark.table(f"{bronze_ods_schema}.contact_details")


# These actually test the data and some will need to do some heavy lifting maybe it is worth labeling them
# some only run maybe on staging where data is kept up to date for example 
@pytest.mark.databricks #dont run in CI environment
@pytest.mark.expensive
# @pytest.mark.skip(reason="Skipping freshness tests in dev")
class TestContactDetailsFreshness:
    """Check data is being loaded daily"""
    
    def test_data_loaded_today(self, contact_details_table):
        """Verify data exists for today's date"""
        # Assuming you have a load_date or update_timestamp column
        # If not, you might check row count changes or use audit table
        today = datetime.now().date()
        
        # Adjust this based on your actual date column
        recent_data = contact_details_table.filter(
            F.col("load_date") == today
        )
        
        row_count = recent_data.count()
        assert row_count > 0, f"No data loaded for {today}"
    
    def test_data_loaded_within_24_hours(self, contact_details_table):
        """Verify data has been refreshed in last 24 hours"""
        yesterday = datetime.now() - timedelta(days=1)
        
        recent_data = contact_details_table.filter(
            F.col("load_date") >= yesterday.date()
        )
        
        row_count = recent_data.count()
        assert row_count > 0, "No data loaded in the last 24 hours"


class TestContactDetailsTelephoneFormat:
    """Validate telephone number formats"""
    
    def test_tel_is_numeric_when_not_null(self, contact_details_table):
        """Tel column should only contain digits when populated"""
        invalid_tel = contact_details_table.filter(
            (F.col("Tel").isNotNull()) & 
            (~F.col("Tel").rlike("^[0-9]+$"))  # Only digits
        )
        
        invalid_count = invalid_tel.count()
        
        if invalid_count > 0:
            # Show examples of bad data for debugging
            invalid_tel.select("OrganisationId", "Tel").show(10, truncate=False)
        
        assert invalid_count == 0, f"Found {invalid_count} telephone numbers with non-numeric characters"
    
    def test_tel_has_valid_uk_length(self, contact_details_table):
        """UK telephone numbers should be 10-11 digits"""
        invalid_length = contact_details_table.filter(
            (F.col("Tel").isNotNull()) &
            ((F.length(F.col("Tel")) < 10) | (F.length(F.col("Tel")) > 11))
        )
        
        invalid_count = invalid_length.count()
        
        if invalid_count > 0:
            invalid_length.select("OrganisationId", "Tel", F.length("Tel").alias("length")).show(10)
        
        assert invalid_count == 0, f"Found {invalid_count} telephone numbers with invalid length"
    
    def test_fax_is_numeric_when_not_null(self, contact_details_table):
        """Fax column should only contain digits when populated"""
        invalid_fax = contact_details_table.filter(
            (F.col("Fax").isNotNull()) & 
            (~F.col("Fax").rlike("^[0-9]+$"))
        )
        
        invalid_count = invalid_fax.count()
        assert invalid_count == 0, f"Found {invalid_count} fax numbers with non-numeric characters"


class TestContactDetailsCompleteness:
    """Check data completeness"""
    
    def test_organisation_id_not_null(self, contact_details_table):
        """OrganisationId is a required field"""
        null_count = contact_details_table.filter(
            F.col("OrganisationId").isNull()
        ).count()
        
        assert null_count == 0, f"Found {null_count} records with null OrganisationId"
    
    def test_at_least_one_contact_method(self, contact_details_table):
        """Each record should have at least one contact method populated"""
        no_contact = contact_details_table.filter(
            F.col("Tel").isNull() &
            F.col("Fax").isNull() &
            F.col("MailTo").isNull() &
            F.col("Http").isNull()
        )
        
        no_contact_count = no_contact.count()
        
        if no_contact_count > 0:
            no_contact.select("OrganisationId").show(10)
        
        assert no_contact_count == 0, f"Found {no_contact_count} records with no contact methods"


class TestContactDetailsDuplicates:
    """Check for duplicate records"""
    
    def test_no_duplicate_organisation_ids(self, contact_details_table):
        """OrganisationId should be unique"""
        duplicate_check = contact_details_table.groupBy("OrganisationId").count()
        duplicates = duplicate_check.filter(F.col("count") > 1)
        
        duplicate_count = duplicates.count()
        
        if duplicate_count > 0:
            duplicates.show(10)
        
        assert duplicate_count == 0, f"Found {duplicate_count} duplicate OrganisationIds"