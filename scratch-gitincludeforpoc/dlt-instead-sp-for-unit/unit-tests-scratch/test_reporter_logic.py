# test_reporter_logic.py


# unit-tests-scratch/test_reporter_logic.py
import sys
import os
from pathlib import Path
import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, LongType

# Add parent directory to path
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir)
# sys.path.insert(0, parent_dir)

############### Make Modules Available  #############
current_dir = Path.cwd()
print(f"Current_dir: {current_dir}")
shared_parent_root = current_dir.parent.resolve()
print(f"shared_parent_root: {shared_parent_root}")
module_folder_path_from_shared_parent = "utils"
module_path = (shared_parent_root / module_folder_path_from_shared_parent).resolve()
print(f"module_path: {module_path}")
if str(module_path) not in sys.path:
    sys.path.insert(0, str(module_path))

######################################################

from reporter_logic import compute_is_reporter



def test_is_reporter_basic(spark):
    # Users
    users = spark.createDataFrame(
        [(1, 10), (2, 20), (3, 30)],
        ["UserBK", "UserHK"]
    )

    # User has location permission
    ual = spark.createDataFrame(
        [(10,)],
        ["UserHK"]
    )

    # User has group permission
    ugr = spark.createDataFrame(
        [(2,)],
        ["userId"]
    )

    # No direct permission
    # DBX doesnt like an empty dataframe
    # uru = spark.createDataFrame(
    #     [],
    #     ["ReportingUserHK"]
    # )

    # No direct permission
    # Define the schema explicitly
    uru_schema = StructType([
        StructField("ReportingUserHK", LongType(), True)
    ])

    uru = spark.createDataFrame(
        [],
        schema=uru_schema  # ✅ Now Spark knows it's a LongType column
    )

    result = compute_is_reporter(users, ual, ugr, uru)

    output = {r.user_id: r.is_reporter for r in result.collect()}

    assert output[1] == 1  # location-based
    assert output[2] == 1  # group-based
    assert output[3] == 0  # no permissions
