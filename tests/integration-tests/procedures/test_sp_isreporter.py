import pytest
from pyspark.sql import SparkSession

# I want to mark it different so it is run by its own cell in the notebook test runner
# i think we probably shouldnt do this
# the code relies on accessing data the data is a test user
# this solution has a dlt function alternative example
@pytest.mark.integration_sql
def test_sp_isreporter(spark):
    df = spark.sql(
        "CALL tel_unified_reporting_gold.sp_isreporter(163598)"
    )
    result = df.collect()[0]["IsReporter"]
    assert result == 1