import random
import pytest
from pathlib import Path
from pyspark.sql import SparkSession
import random
from pyspark.dbutils import DBUtils


###############################
## This is more integration now anyway i need a core function test for unit
## Spark and dbutils are not going to work in git
## Routing wont work in git actions
## Need to move things into testing config
## need to move thing into toml
## file needs to be in correct location
##############################


from utils import load_csv_table


######################################
### PyTest doesnt have access to spark and dbutils in the same way so we are checking the test setup here ###
######################################

@pytest.fixture(scope="function")
def test_dbfs_setup(spark):
    """
    Fixture to handle the setup and teardown of DBFS test data.
    This keeps the actual test function clean.
    """
    dbutils = DBUtils(spark)
    test_id = random.randint(10000, 99999)
    dbfs_folder = f"/tmp/test_csv_{test_id}"
    filename = "Contact_Details.csv"
    
    # --- SETUP: Create a real CSV file ---
    test_data = [
        ("ORG001", "Test Hospital", "Active"),
        ("ORG002", "Test Clinic", "Inactive"),
        ("ORG003", "Test Surgery", "Active")
    ]
    columns = ["OrganisationID", "Name", "Status"]
    test_df = spark.createDataFrame(test_data, columns)
    
    # Write to temp then move to make it a 'proper' single CSV file
    temp_path = f"{dbfs_folder}/temp"
    test_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(temp_path)
    
    part_file = [f.path for f in dbutils.fs.ls(temp_path) if f.path.endswith('.csv')][0]
    final_path = f"{dbfs_folder}/{filename}"
    dbutils.fs.cp(part_file, final_path)
    
    # Provide the path to the test
    yield f"dbfs:{dbfs_folder}/", filename
    
    # --- TEARDOWN: Cleanup after test ---
    dbutils.fs.rm(dbfs_folder, recurse=True)

def test_load_csv_table_using_dbfs(spark, test_dbfs_setup):
    """
    Test loading CSV from DBFS using the logic from src/utils.
    """
    # Unpack the fixture values
    base_path, filename = test_dbfs_setup
    
    # ACT: Run the actual function from your src/utils
    df = load_csv_table(spark, base_path, filename)
    
    # ASSERT
    assert df.count() == 3
    assert "OrganisationID" in df.columns
    
    first_row = df.collect()[0]
    assert first_row["OrganisationID"] == "ORG001"
    print(f"✅ Successfully verified {filename} at {base_path}")

################### DEL below just in because poc ##########################

# def test_load_csv_table_using_dbfs(spark):
#     """
#     Test loading CSV from DBFS - THIS SHOULD WORK
#     """
#     dbutils = DBUtils(spark)
    
#     # Create test data
#     test_data = [
#         ("ORG001", "Test Hospital", "Active"),
#         ("ORG002", "Test Clinic", "Inactive"),
#         ("ORG003", "Test Surgery", "Active")
#     ]
#     columns = ["OrganisationID", "Name", "Status"]
#     test_df = spark.createDataFrame(test_data, columns)
    
#     # Write to DBFS
#     test_id = random.randint(10000, 99999)
#     dbfs_path = f"/tmp/test_dbfs_{test_id}"
#     filename = "Contact_Details.csv"
    
#     # Write using Spark (creates directory with part files)
#     test_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(dbfs_path)
    
#     print(f"✓ Wrote to DBFS: {dbfs_path}")
    
#     # Setup paths
#     test_id = random.randint(10000, 99999)
#     dbfs_folder = f"/tmp/test_dbfs_{test_id}"
#     filename = "Contact_Details.csv"
    
#     # STEP 1: Write to temporary location (Spark creates part files)
#     temp_write_path = f"{dbfs_folder}/temp_write"
#     test_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(temp_write_path)
    
#     print(f"✓ Wrote to temp location: {temp_write_path}")
    
#     # STEP 2: Find the actual CSV part file that was created
#     files = dbutils.fs.ls(temp_write_path)
#     csv_part_file = [f.path for f in files if f.path.endswith('.csv')][0]
    
#     print(f"✓ Found part file: {csv_part_file}")
    
#     # STEP 3: Copy it to a proper filename
#     final_csv_path = f"{dbfs_folder}/{filename}"
#     dbutils.fs.cp(csv_part_file, final_csv_path)
    
#     print(f"✓ Copied to proper filename: {final_csv_path}")
    
#     # Test our function with DBFS path
#     base_path = f"dbfs:{dbfs_folder}/"
#     df = load_csv_table(spark, base_path, filename)
#     # worked but its using partials files in a folder directory - i want to test with an actual full file
#     # df = load_csv_table_copy(spark, base_path, "")  # Empty filename since Spark reads the whole directory
    
#     print(f"✓ Loaded using: load_csv_table(spark, '{base_path}', '{filename}')")
#     df.show()
    
#     # Assertions
#     assert df.count() == 3, f"Expected 3 rows, got {df.count()}"
#     assert "OrganisationID" in df.columns
#     assert "Name" in df.columns
#     assert "Status" in df.columns
    
#     first_row = df.collect()[0]
#     assert first_row["OrganisationID"] == "ORG001"
    
#     # Cleanup
#     dbutils.fs.rm(dbfs_path, recurse=True)
#     print("✅ DBFS test PASSED!")