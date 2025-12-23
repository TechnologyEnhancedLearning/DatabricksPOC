import pytest
from pyspark.sql import SparkSession


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


### Worked but want something that can work with cicd
# import pytest
# from pyspark.sql import SparkSession

# # Use existing Spark session in Databricks (Spark Connect)
# @pytest.fixture(scope="session")
# def spark():
#     session = SparkSession.getActiveSession()
#     if session is None:
#         raise RuntimeError("No active Spark session found. Ensure you are running in Databricks.")
#     return session