# test_reporter_logic.py


# unit-tests-scratch/test_reporter_logic.py
import sys
from pathlib import Path
import pytest
from pyspark.sql import SparkSession

############### Make Modules Available  #############
# Use __file__ instead of cwd() for reliability
test_file_dir = Path(__file__).parent.resolve()
print(f"Test file directory: {test_file_dir}")

# Go up to the folder containing the module
parent_dir = test_file_dir.parent.resolve()
print(f"Parent directory: {parent_dir}")

# Add to path if not already there
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))
    print(f"Added to sys.path: {parent_dir}")
######################################################

from path.to.reporter_logic import compute_is_reporter



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
    uru = spark.createDataFrame(
        [],
        ["ReportingUserHK"]
    )

    result = compute_is_reporter(users, ual, ugr, uru)

    output = {r.user_id: r.is_reporter for r in result.collect()}

    assert output[1] == 1  # location-based
    assert output[2] == 1  # group-based
    assert output[3] == 0  # no permissions
