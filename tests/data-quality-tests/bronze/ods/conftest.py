# conftest is addative so we could set and inject from here
# the only reason for not is though it reduces duplicating it in test files it seemed and extra bit of cognitive load for now

# data-tests/silver/ods/conftest.py
# @pytest.fixture(scope="session")
# def silver_ods_schema(spark):
#     catalog = spark.conf.get("bundle.catalog", "dev_catalog")
#     prefix = spark.conf.get("bundle.schema_prefix", "")
#     return f"{catalog}.{prefix}silver_ods"
# 

# and then injected in test file
# def  test_tel_is_numeric(spark, bronze_ods_schema):
#     df = spark.table(f"{bronze_ods_schema}.contact_details")