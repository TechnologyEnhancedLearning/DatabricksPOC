"""Unit tests for data loading utilities"""

# []()

# qqqq TODO this is very AI generated run it past someone make it more relevant for data team
# need to review some examples and refactor todo qqqq
import pytest
import tempfile
import os
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
#from pyspark.sql.types import StringType, IntegerType
from src.utils.loaders import load_csv_table
from pathlib import Path
# Helper function for dbutils access (used for cleanup)
# def get_dbutils(spark: SparkSession):
#     """Safely get dbutils for cleaning up files on DBFS."""
#     try:
#         # Databricks Connect (the likely scenario for your tests)
#         return spark.sparkContext._jvm.com.databricks.dbutils_v1.DBUtilsHolder.dbutils
#     except Exception:
#         # Fallback (for completeness, though Connect should be the priority)
#         return None 

# @pytest.fixture
# def sample_csv_data(spark: SparkSession, tmp_path: Path):
#     """
#     1. Creates CSV data locally (using pytest's tmp_path).
#     2. Stages the data onto DBFS using the 'file://' protocol.
#     3. Cleans up the DBFS files afterward using dbutils.
#     """
#     csv_filename = "test_data.csv"
#     csv_file_local = tmp_path / csv_filename
    
#     # 1. Create CSV locally
#     csv_content = """OrganisationID,Name,Status
# ORG001,Test Hospital,Active
# ORG002,Test Clinic,Inactive
# ORG003,Test Surgery,Active"""
#     csv_file_local.write_text(csv_content)
    
#     # 2. Define the unique DBFS staging directory
#     dbfs_dir_path = f"dbfs:/tmp/{tmp_path.name}/" 
    
#     # --- Data Staging (The fix is here) ---
#     print(f"\n[INFO] Staging data from LOCAL: file://{str(csv_file_local)} to REMOTE: {dbfs_dir_path}")
    
#     try:
#         spark.read.format("csv") \
#             .option("header", "true") \
#             .option("inferSchema", "true") \
#             .load(f"file://{str(csv_file_local)}") \
#             .write.format("csv") \
#             .option("header", "true") \
#             .mode("overwrite") \
#             .save(dbfs_dir_path)
#     except Exception as e:
#         print(f"[ERROR] Spark write failed during staging: {e}")
#         raise # Re-raise the exception to fail the test setup
        
#     # 3. Return the path to the test function (without the 'dbfs:' prefix)
#     dbfs_base_path_for_load = f"/tmp/{tmp_path.name}/"
    
#     # --- YIELD (Test Execution) and CLEANUP (Teardown) ---
#     try:
#         yield dbfs_base_path_for_load, csv_filename
#     finally:
#         # 4. Clean up the files on DBFS
#         print(f"\n[INFO] Starting DBFS cleanup for: {dbfs_dir_path}")
#         try:
#             dbutils = get_dbutils(spark)
#             if dbutils:
#                 dbutils.fs.rm(dbfs_dir_path, True)
#                 print(f"[INFO] DBFS cleanup complete.")
#             else:
#                 print("[WARN] Could not retrieve dbutils. Skipping DBFS cleanup.")
#         except Exception as e:
#             print(f"[WARN] Failed to clean up DBFS path {dbfs_dir_path}. Manual cleanup may be required. Error: {e}")

# finds it but no permission
# @pytest.fixture
# def sample_csv_data():
#     """
#     Returns the paths needed to read the static CSV file located in the repo 
#     fixtures folder, ensuring the 'file://' prefix is used.
    
#     NOTE: Assumes you have created the file at: 
#     'tests/unit-tests/utils/fixtures/org_data.csv'
#     """
#     # --- Configuration (Adjust relative path if needed) ---
#     csv_filename = "org_data.csv"
#     fixture_dir = "tests/unit-tests/utils/fixtures" 
    
#     # 1. Calculate the absolute path on the driver's local disk
#     # This finds the file's true physical location
#     absolute_base_path = Path(os.getcwd()) / fixture_dir

#     # 2. CRITICAL FIX: Add 'file://' prefix to override the DBFS assumption
#     # Path must end with a slash for your function's concatenation to work.
#     base_path_with_protocol = f"file://{str(absolute_base_path)}/"
    
#     return base_path_with_protocol, csv_filename
@pytest.fixture
def sample_csv_data(spark: SparkSession, tmp_path: Path):
    """
    STAGES the static CSV file to a temporary DBFS location 
    to bypass the WorkspaceLocalFileSystem security restriction.
    """
    # 1. Define Paths
    csv_filename = "org_data.csv"
    fixture_dir = "tests/unit-tests/utils/fixtures" 
    
    # Path to the file on the local driver disk (where it currently lives)
    local_base_path = Path(os.getcwd()) / fixture_dir
    local_file_path = local_base_path / csv_filename
    
    # Define the TEMPORARY path on DBFS
    # We use tmp_path name to ensure uniqueness, but put it on DBFS
    dbfs_staging_path = f"dbfs:/tmp/pytest_data/{tmp_path.name}/"
    dbfs_file_path = dbfs_staging_path + csv_filename 

    # 2. Check and Write the CSV content locally (if you haven't done it yet)
    csv_content = """OrganisationID,Name,Status
ORG001,Test Hospital,Active
ORG002,Test Clinic,Inactive
ORG003,Test Surgery,Active"""
    
    local_base_path.mkdir(parents=True, exist_ok=True)
    local_file_path.write_text(csv_content) # Writes file to local driver disk

    # 3. CRITICAL STEP: COPY the file from Local Disk to DBFS
    try:
        # Access dbutils via SparkSession for Pytest compatibility
        dbutils = spark.dbutils
        # Source path MUST start with 'file:' prefix for dbutils.fs.cp to find the local file
        dbutils.fs.cp(f"file://{str(local_file_path)}", dbfs_file_path, recurse=True)
    except Exception as e:
        # Cleanup DBFS folder even if copy failed
        try:
            dbutils.fs.rm(dbfs_staging_path, recurse=True)
        except:
            pass
        raise RuntimeError(f"Failed to stage file to DBFS. Error: {e}")

    # 4. Return the DBFS path (No 'file://' needed, as it is now cloud storage)
    # This base_path is now the DBFS staging folder path
    return dbfs_staging_path, csv_filename

# @pytest.fixture
# def sample_csv_data(spark: SparkSession, tmp_path: Path):
#     """
#     Uses Spark to write mock CSV data to a temporary, local directory.
#     This guarantees Spark can read it back during the test.
#     """
#     # 1. Define the unique temporary folder path
#     temp_folder_path = tmp_path / "test_csv_input"
    
#     # 2. Define the mock data
#     data = [
#         ("ORG001", "Test Hospital", "Active"),
#         ("ORG002", "Test Clinic", "Inactive"),
#         ("ORG003", "Test Surgery", "Active")
#     ]
#     columns = ["OrganisationID", "Name", "Status"]

#     # 3. Write the DataFrame to the temporary folder using Spark
#     spark.createDataFrame(data, columns).write.csv(
#         path=str(temp_folder_path),
#         header=True,
#         mode="overwrite"
#     )
    
#     # 4. Return the path components
#     # We return the folder path as base_path, and we can keep the original filename
#     # for the test signature, even though the function ignores it now.
#     return str(temp_folder_path) + "/", "test_data.csv"

# @pytest.fixture
# def sample_csv_data(tmp_path):
#     """Create a sample CSV file for testing"""
#     # Create a temporary CSV file
#     csv_file = tmp_path / "test_data.csv"
#     csv_content = """OrganisationID,Name,Status
# ORG001,Test Hospital,Active
# ORG002,Test Clinic,Inactive
# ORG003,Test Surgery,Active"""

#     csv_file.write_text(csv_content)
    
#     return str(tmp_path) + "/", "test_data.csv"




def test_load_csv_table_basic(spark: SparkSession, sample_csv_data):


    """Test that load_csv_table loads CSV correctly"""
    base_path, csv_filename = sample_csv_data

    # Load the CSV
    # temp solution

    df = load_csv_table(spark, base_path, csv_filename)

    # Verify the DataFrame was created
    assert df is not None

    # Verify row count
    assert df.count() == 3

    # Verify columns exist
    columns = df.columns
    assert "OrganisationID" in columns
    assert "Name" in columns
    assert "Status" in columns
    
# def get_spark() -> SparkSession:
#     try:
#         from databricks.connect import DatabricksSession
#         return DatabricksSession.builder.serverless(True).getOrCreate()
#     except ImportError:
#         return SparkSession.builder.getOrCreate()

# def get_spark() -> SparkSession:
#     """Get Spark session - use local for testing"""
#     return (
#         SparkSession.builder
#         .master("local[*]")
#         .appName("unit-tests")
#         .config("spark.sql.warehouse.dir", "/tmp/spark-warehouse")
#         .getOrCreate()
#     )
# def get_spark() -> SparkSession:
#     """Get Spark session - use notebook's existing session"""
#     return SparkSession.getActiveSession() or SparkSession.builder.getOrCreate()

# def test_load_csv_table_data_content(spark, sample_csv_data):
#     """Test that load_csv_table loads correct data"""
#     base_path, csv_filename = sample_csv_data

#     # Load the CSV
#     df = load_csv_table(base_path, csv_filename)

#     # Collect data and verify content
#     rows = df.collect()

#     # Check first row
#     assert rows[0]["OrganisationID"] == "ORG001"
#     assert rows[0]["Name"] == "Test Hospital"
#     assert rows[0]["Status"] == "Active"

#     # Check second row
#     assert rows[1]["OrganisationID"] == "ORG002"
#     assert rows[1]["Status"] == "Inactive"


# def test_load_csv_table_schema_inference(spark, sample_csv_data):
#     """Test that schema inference works correctly"""
#     base_path, csv_filename = sample_csv_data

#     # Load the CSV
#     df = load_csv_table(base_path, csv_filename)

#     # Verify schema was inferred
#     schema = df.schema
#     assert len(schema.fields) == 3

#     # All fields should be strings in this case
#     for field in schema.fields:
#         assert field.dataType == StringType()


# def test_load_csv_table_with_numeric_data(spark, tmp_path):
#     """Test CSV loading with numeric columns"""
#     # Create CSV with numeric data
#     csv_file = tmp_path / "numeric_data.csv"
#     csv_content = """ID,Count,Value
# 1,100,25.5
# 2,200,30.75
# 3,150,22.25"""

#     csv_file.write_text(csv_content)

#     # Load the CSV
#     df = load_csv_table(str(tmp_path) + "/", "numeric_data.csv")

#     # Verify numeric types were inferred
#     schema = df.schema
#     id_field = [f for f in schema.fields if f.name == "ID"][0]
#     count_field = [f for f in schema.fields if f.name == "Count"][0]
#     value_field = [f for f in schema.fields if f.name == "Value"][0]

#     # Check that numeric columns were inferred as integers or doubles
#     assert id_field.dataType == IntegerType()
#     assert count_field.dataType == IntegerType()
#     # Value field should be double since it has decimals
#     assert "Double" in str(value_field.dataType)


# def test_load_csv_table_empty_file(spark, tmp_path):
#     """Test handling of CSV with only headers"""
#     csv_file = tmp_path / "empty_data.csv"
#     csv_content = """OrganisationID,Name,Status"""

#     csv_file.write_text(csv_content)

#     # Load the CSV
#     df = load_csv_table(str(tmp_path) + "/", "empty_data.csv")

#     # Should have columns but no rows
#     assert len(df.columns) == 3
#     assert df.count() == 0


# def test_load_csv_table_file_not_found(spark, tmp_path):
#     """Test error handling when file doesn't exist"""
#     with pytest.raises(Exception):
#         load_csv_table(str(tmp_path) + "/", "nonexistent_file.csv")