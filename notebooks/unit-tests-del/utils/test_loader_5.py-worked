import sys, os
import shutil
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

# we need better routing
PROJECT_ROOT = "/Workspace/Users/philip.tate@nhs.net/PT Separate Feature Branch/src"
sys.path.insert(0, PROJECT_ROOT)

from utils import load_csv_table


######################################
### PyTest doesnt have access to spark and dbutils in the same way so we are checking the test setup here ###
######################################

# Use existing Spark session in Databricks (Spark Connect)
@pytest.fixture(scope="session")
def spark():
    session = SparkSession.getActiveSession()
    if session is None:
        raise RuntimeError("No active Spark session found. Ensure you are running in Databricks.")
    return session

def test_load_csv_table_function_using_dbfs(spark):
    """
    Test loading CSV from DBFS - THIS SHOULD WORK
    """
    dbutils = DBUtils(spark)
    
    # Create test data
    test_data = [
        ("ORG001", "Test Hospital", "Active"),
        ("ORG002", "Test Clinic", "Inactive"),
        ("ORG003", "Test Surgery", "Active")
    ]
    columns = ["OrganisationID", "Name", "Status"]
    test_df = spark.createDataFrame(test_data, columns)
    
    # Write to DBFS
    test_id = random.randint(10000, 99999)
    dbfs_path = f"/tmp/test_dbfs_{test_id}"
    filename = "Contact_Details.csv"
    
    # Write using Spark (creates directory with part files)
    test_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(dbfs_path)
    
    print(f"✓ Wrote to DBFS: {dbfs_path}")
    
    # Setup paths
    test_id = random.randint(10000, 99999)
    dbfs_folder = f"/tmp/test_dbfs_{test_id}"
    filename = "Contact_Details.csv"
    
    # STEP 1: Write to temporary location (Spark creates part files)
    temp_write_path = f"{dbfs_folder}/temp_write"
    test_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(temp_write_path)
    
    print(f"✓ Wrote to temp location: {temp_write_path}")
    
    # STEP 2: Find the actual CSV part file that was created
    files = dbutils.fs.ls(temp_write_path)
    csv_part_file = [f.path for f in files if f.path.endswith('.csv')][0]
    
    print(f"✓ Found part file: {csv_part_file}")
    
    # STEP 3: Copy it to a proper filename
    final_csv_path = f"{dbfs_folder}/{filename}"
    dbutils.fs.cp(csv_part_file, final_csv_path)
    
    print(f"✓ Copied to proper filename: {final_csv_path}")
    
    # Test our function with DBFS path
    base_path = f"dbfs:{dbfs_folder}/"
    df = load_csv_table(spark, base_path, filename)
    # worked but its using partials files in a folder directory - i want to test with an actual full file
    # df = load_csv_table_copy(spark, base_path, "")  # Empty filename since Spark reads the whole directory
    
    print(f"✓ Loaded using: load_csv_table(spark, '{base_path}', '{filename}')")
    df.show()
    
    # Assertions
    assert df.count() == 3, f"Expected 3 rows, got {df.count()}"
    assert "OrganisationID" in df.columns
    assert "Name" in df.columns
    assert "Status" in df.columns
    
    first_row = df.collect()[0]
    assert first_row["OrganisationID"] == "ORG001"
    
    # Cleanup
    dbutils.fs.rm(dbfs_path, recurse=True)
    print("✅ DBFS test PASSED!")

#######################################################
######################################################
## Junk because poc but very small chance useful for what tried if issues soon
########################################################
#### not accessible by spark
# Fixture to create a temporary CSV for testing
# @pytest.fixture
# def mock_csv_data(spark, tmp_path):
#     # Sample data
#     data = [
#         ("ORG001", "Test Hospital", "Active"),
#         ("ORG002", "Test Clinic", "Inactive"),
#         ("ORG003", "Test Surgery", "Active")
#     ]
#     columns = ["OrganisationID", "Name", "Status"]
#     test_df = spark.createDataFrame(data, columns)

#     # Unique temp folder
#     test_id = random.randint(10000, 99999)
#     temp_path = tmp_path / f"test_csv_{test_id}"
#     temp_path.mkdir(parents=True, exist_ok=True)

#     # Databricks-safe CSV write: convert to Pandas and write
#     csv_path = temp_path / "Contact_Details.csv"
#     test_df.toPandas().to_csv(csv_path, index=False)

#     yield str(temp_path), "Contact_Details.csv"

#     # Cleanup
#     shutil.rmtree(temp_path, ignore_errors=True)

# # Example test using the fixture
# def test_csv_exists(mock_csv_data):
#     folder, filename = mock_csv_data
#     full_path = os.path.join(folder, filename)
#     print(f"Checking CSV file exists at: {full_path}")
#     assert os.path.exists(full_path)

# Example using dbutils worked
# def test_dbutils_write_and_read_simple(spark):
#     """
#     Simple test: Can we write a CSV to DBFS and read it back with Spark?
#     This proves the core concept works.
#     """
#     from pyspark.dbutils import DBUtils
#     dbutils = DBUtils(spark)

#         # 0. CLEAN UP ANY STALE DATA FIRST
#     test_path = "/tmp/simple_test_12345"
#     try:
#         dbutils.fs.rm(test_path, recurse=True)
#         print(f"✓ Cleaned up stale data at: {test_path}")
#     except:
#         print(f"✓ No stale data to clean")

#     # 1. Create test data
#     test_data = [("A", 1), ("B", 2), ("C", 3)]
#     test_df = spark.createDataFrame(test_data, ["letter", "number"])
    
#     # 2. Write to DBFS using Spark
#     test_path = "/tmp/simple_test_12345"
#     test_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(test_path)
    
#     print(f"✓ Wrote CSV to: {test_path}")
    
#     # 3. Check it exists using dbutils
#     files = dbutils.fs.ls(test_path)
#     print(f"✓ Files in DBFS: {[f.name for f in files]}")
    
#     # 4. Read it back using Spark
#     df_read = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(f"dbfs:{test_path}")
    
#     print(f"✓ Read back {df_read.count()} rows")
#     df_read.show()
    
#     # 5. Verify data
#     assert df_read.count() == 3
#     assert "letter" in df_read.columns
#     assert "number" in df_read.columns
    
#     # 6. Cleanup
#     dbutils.fs.rm(test_path, recurse=True)
#     print(f"✓ Cleaned up: {test_path}")
    
#     print("✅ SUCCESS: dbutils works in .py file, can write and read from DBFS!")

####################################################################
#### Using our test CSV test the loader function
########################################################
#################################################
## Hardcode in function for now instead of reference
###################################################
## This is what we want to use ultimately
# df = load_csv_table(spark, folder + "/", filename)
# def load_csv_table_copy(spark, base_path, csv_filename):
#     """Load CSV from Azure storage with standard options
    
#     Args:
#         base_path: Base path to the folder containing CSV files
#         csv_filename: Name of the CSV file to load
        
#     Returns:
#         DataFrame: Spark DataFrame with CSV data
#     """
    
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(f"{base_path}{csv_filename}")
#     )

# # Actual test using the fixture
# def test_load_csv_table_function(spark, mock_csv_data):
#     folder, filename = mock_csv_data

#     print("Folder path:", folder)
#     print("Filename:", filename)
#     full_path = folder + "/" + filename
#     print("Full CSV path passed to loader:", full_path)
#     print("Does file exist?", os.path.exists(full_path))

#     # Load using your function


#     df = load_csv_table_copy(spark, folder + "/", filename)


#     # Print DataFrame schema and first few rows
#     print("DataFrame schema:")
#     df.printSchema()
#     print("First 5 rows:")
#     df.show(5)

#     # Assertions
#     assert df is not None, "DataFrame should not be None"
#     count = df.count()
#     print("Row count:", count)
#     assert count == 3, f"Expected 3 rows, got {count}"
#     assert "OrganisationID" in df.columns
#     assert "Name" in df.columns
#     assert "Status" in df.columns

#     # Check first row
#     first_row = df.collect()[0]
#     print("First row:", first_row.asDict())
#     assert first_row["OrganisationID"] == "ORG001"
#     assert first_row["Name"] == "Test Hospital"
#     assert first_row["Status"] == "Active"


# %pip install -e "/Workspace/Repos/philip.tate@nhs.net/PT Separate Feature Branch"
# %pip install pytest>=7.0
# !python -m pytest # tests/unit-tests/ -v -p no:cacheprovider
# import os
# os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
# import pytest
# tests_path = "/Workspace/Repos/philip.tate@nhs.net/PT Separate Feature Branch/tests/unit-tests/"
# !python -m pytest tests/unit-tests/ -v -p no:cacheprovider
# pytest.main([tests_path, "-v", "-p", "no:cacheprovider"])