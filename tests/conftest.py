import pytest
from pyspark.sql import SparkSession

# Use existing Spark session in Databricks (Spark Connect)
@pytest.fixture(scope="session")
def spark():
    session = SparkSession.getActiveSession()
    if session is None:
        raise RuntimeError("No active Spark session found. Ensure you are running in Databricks.")
    return session