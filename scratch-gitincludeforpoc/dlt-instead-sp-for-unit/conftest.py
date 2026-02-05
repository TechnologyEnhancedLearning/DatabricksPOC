import pytest
from pyspark.sql import SparkSession

# spark isnt in github by default like databricks so we need to create it
@pytest.fixture(scope="session")
def spark():
    # Databricks / Spark Connect
    session = SparkSession.getActiveSession()
    if session is not None:
        yield session
        return

    # Local / CI Spark
    spark = (
        SparkSession.builder
        .master("local[1]")
        .appName("pytest-pyspark")
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )

    yield spark
    spark.stop()