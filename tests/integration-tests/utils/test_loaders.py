import pytest
import uuid
from datetime import datetime
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils
import os

###############################
## This is more integration now anyway i need a core function test for unit
## Spark and dbutils are not going to work in git
### - but this actually integration so just triggered by git
## dbutils storage actually outside governance
## my privilages but not service principle privilages can access ddfs storage
## [medium article dbfs-> volumes](https://medium.com/towards-data-engineering/when-dbfs-is-not-an-option-how-databricks-volumes-saved-the-day-for-file-based-learning-on-free-a0e0e92579ce)
##############################


from utils import load_csv_table


######################################
### PyTest doesnt have access to spark and dbutils in the same way so we are checking the test setup here ###
######################################

@pytest.fixture(scope="function")
def test_loaders_setup(spark):
    """
    Fixture to handle the setup and teardown of DBFS test data.
    This keeps the actual test function clean.
    """
    catalog = os.getenv("CATALOG")
    volume_name = "integration_testing"

    dbutils = DBUtils(spark)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    run_id = f"{timestamp}_{uuid.uuid4()}"
    
    #/Volumes/dev_catalog/temp/integration_tests/run_000100
    temp_vol_run_path = f"/Volumes/{catalog}/temp/{volume_name}/run_{run_id}"
    filename = "Contact_Details.csv"
    
    print(f"Creating test folder in volume:\n{temp_vol_run_path}")
    dbutils.fs.mkdirs(temp_vol_run_path)
    
    # --- SETUP: Create a real CSV file ---
    test_data = [
        ("ORG001", "Test Hospital", "Active"),
        ("ORG002", "Test Clinic", "Inactive"),
        ("ORG003", "Test Surgery", "Active")
    ]
    columns = ["OrganisationID", "Name", "Status"]
    test_df = spark.createDataFrame(test_data, columns)
    
    # Write to temp then move to make it a 'proper' single CSV file
       # --------------------------
    # WRITE CSV
    # --------------------------
    # Spark writes CSV as a folder with part-0000*.csv

    ### Works under high privilidge user not service principle, dbfs not governed
    #temp_path = f"{dbfs_folder}/temp"
    #test_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(temp_vol_run_path)
    #part_file = [f.path for f in dbutils.fs.ls(temp_path) if f.path.endswith('.csv')][0]
    #final_path = f"{dbfs_folder}/{filename}"
    #dbutils.fs.cp(part_file, final_path)
    # Provide the path to the test
    #yield f"dbfs:{dbfs_folder}/", filename
 # # Provide the path to the test
    # yield f"dbfs:{dbfs_folder}/", filename
    
    # # --- TEARDOWN: Cleanup after test ---
    # dbutils.fs.rm(dbfs_folder, recurse=True)

    test_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(temp_vol_run_path)
    
    part_file = [f.path for f in dbutils.fs.ls(temp_vol_run_path) if f.path.endswith('.csv')][0]
    final_path = f"{temp_vol_run_path}/{filename}"
    dbutils.fs.cp(part_file, final_path)
    

  
    print(f"✅ CSV created at: {final_path}")
    
    # --------------------------
    # YIELD TO TEST
    # --------------------------
    yield temp_vol_run_path, filename
    
    # --------------------------
    # TEARDOWN
    # --------------------------
    dbutils.fs.rm(temp_vol_run_path, recurse=True)
    print(f"✅ Cleaned up test folder: {temp_vol_run_path}")
   

def test_load_csv_table(spark, test_loaders_setup):
    """
    Test loading CSV from DBFS using the logic from src/utils.
    """
    # Unpack the fixture values
    base_path, filename = test_loaders_setup
    
    # ACT: Run the actual function from your src/utils
    df = load_csv_table(spark, base_path, filename)
    
    # ASSERT
    assert df.count() == 3
    assert "OrganisationID" in df.columns
    
    first_row = df.collect()[0]
    assert first_row["OrganisationID"] == "ORG001"
    print(f"✅ Successfully verified {filename} at {base_path}")
