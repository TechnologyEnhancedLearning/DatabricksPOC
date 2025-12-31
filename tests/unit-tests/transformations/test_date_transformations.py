# test_working_days_monthly.py
# qqqq retrospect pyspark test may be better
import sys
import pytest
from pyspark.sql import SparkSession
from pyspark.sql import functions as fn


from transformations import working_days_monthly

@pytest.fixture(scope="function")
def working_days_calendar(spark):
    """
    Create a calendar DataFrame with monthly working days.
    Covers 10 years from 2020-01-01.
    Excludes weekends as non-working days.
    Prints sample data for debugging.
    """
    
    df = spark.range(0, 365 * 10).select(
        fn.expr("date_add('2020-01-01', cast(id as int))").alias("Date")
    ).withColumn(
        "Month_Start", fn.trunc("Date", "MM")
    ).withColumn(
        "Working_Day_Type",
        fn.when(fn.date_format("Date", "EEEE").isin("Saturday", "Sunday"), "N").otherwise("Y")
    ).withColumn(
        "Working_Day_Calc",
        fn.when(fn.col("Working_Day_Type") == "Y", 1).otherwise(0)
    )

    # DEBUG: Print the schema and a small sample of data
    # print("\n=== Calendar Schema ===")
    # df.printSchema()
    # print("\n=== Calendar Sample Data ===")
    # df.orderBy("Date").show(12, truncate=False)

    # Optional: Aggregate by month to get total working days
    cal_agg = df.groupBy("Month_Start").agg(
        fn.sum("Working_Day_Calc").alias("Total_Working_Days")
    )

    # DEBUG: Print aggregated result
    # print("\n=== Aggregated Calendar Sample ===")
    # cal_agg.orderBy("Month_Start").show(12, truncate=False)

    return cal_agg


@pytest.fixture(scope="function")
def sample_dataframe_january_2023(spark):
    """
    Fixture providing a simple test dataframe for January 2023
    """
    data = [("2023-01-01",)]
    columns = ["start_date"]
    return spark.createDataFrame(data, columns)


@pytest.fixture(scope="function")
def sample_dataframe_multiple_months(spark):
    """
    Fixture providing a dataframe with multiple months
    """
    data = [
        ("2023-01-01",),
        ("2023-02-01",),
        ("2023-03-01",),
    ]
    columns = ["start_date"]
    return spark.createDataFrame(data, columns)


@pytest.fixture(scope="function")
def sample_dataframe_with_extra_columns(spark):
    """
    Fixture providing a dataframe with additional columns beyond start_date
    """
    data = [
        ("2023-01-01", "ORG001", 100),
        ("2023-02-01", "ORG002", 200),
    ]
    columns = ["start_date", "org_id", "value"]
    return spark.createDataFrame(data, columns)


# ============================================================================
# TESTS
# ============================================================================

def test_working_days_adds_column(working_days_calendar, sample_dataframe_january_2023):
    """
    Test that working_days_monthly adds the working_days column
    """
    # ACT
    result_df = working_days_monthly(working_days_calendar, sample_dataframe_january_2023, "start_date")
    
    # ASSERT
    assert "working_days" in result_df.columns, "working_days column should be added"
    assert result_df.count() == 1, f"Expected 1 row, got {result_df.count()}"
    
    print("✅ Column added successfully")


def test_working_days_january_2023_count(working_days_calendar, sample_dataframe_january_2023):
    """
    Test that January 2023 returns 22 working days
    January 2023: 31 days - 4 Saturdays - 5 Sundays = 22 working days
    """
    # ACT
    result_df = working_days_monthly(working_days_calendar, sample_dataframe_january_2023, "start_date")
    
    # ASSERT
    working_days = result_df.collect()[0]["working_days"]
    assert working_days == 22, f"January 2023 should have 22 working days, got {working_days}"
    
    print(f"✅ January 2023 verified: {working_days} working days")

# Just trying out pytest.mark so can exclude by run: pytest -m "not databricks" but the intention would be unit tests via github action and integration by github action triggering test in databricks environment
@pytest.mark.databricks
def test_working_days_february_2023_count(spark,working_days_calendar):
    """
    Test that February 2023 returns 20 working days
    February 2023: 28 days - 4 Saturdays - 4 Sundays = 20 working days
    """
    # ARRANGE
    data = [("2023-02-01",)]
    columns = ["start_date"]
    input_df = spark.createDataFrame(data, columns)
    
    # ACT
    result_df = working_days_monthly(working_days_calendar, input_df, "start_date")
    
    # ASSERT
    working_days = result_df.collect()[0]["working_days"]
    assert working_days == 20, f"February 2023 should have 20 working days, got {working_days}"
    
    print(f"✅ February 2023 verified: {working_days} working days")


def test_working_days_multiple_months(working_days_calendar, sample_dataframe_multiple_months):
    """
    Test that function handles multiple months correctly
    """
    # ACT
    result_df = working_days_monthly(working_days_calendar, sample_dataframe_multiple_months, "start_date")
    
    # ASSERT
    assert result_df.count() == 3, "Should have 3 rows"
    
    # All rows should have positive working days
    results = result_df.collect()
    for row in results:
        assert row["working_days"] > 0, f"All rows should have positive working days"
        assert row["working_days"] <= 23, f"Working days should be reasonable"
    
    print("✅ Multiple months handled correctly")


def test_working_days_preserves_columns(working_days_calendar, sample_dataframe_with_extra_columns):
    """
    Test that function preserves existing columns
    """
    # ACT
    result_df = working_days_monthly(working_days_calendar, sample_dataframe_with_extra_columns, "start_date")
    
    # ASSERT
    assert "start_date" in result_df.columns, "Original start_date column should be preserved"
    assert "org_id" in result_df.columns, "org_id column should be preserved"
    assert "value" in result_df.columns, "value column should be preserved"
    assert "working_days" in result_df.columns, "working_days column should be added"
    
    # Check data integrity
    first_row = result_df.filter(fn.col("org_id") == "ORG001").collect()[0]
    assert first_row["value"] == 100, "Original data should be preserved"
    assert first_row["working_days"] > 0, "Working days should be calculated"
    
    print("✅ All columns preserved correctly")


def test_working_days_with_null_dates(spark,working_days_calendar):
    """
    Test handling of null dates (edge case)
    """
    # ARRANGE
    data = [
        ("2023-01-01",),
        (None,),
        ("2023-02-01",),
    ]
    columns = ["start_date"]
    input_df = spark.createDataFrame(data, columns)
    
    # ACT
    result_df = working_days_monthly(working_days_calendar, input_df, "start_date")
    
    # ASSERT
    assert result_df.count() == 3, "Should handle null dates without dropping rows"
    
    # Null date should have 0 working days (due to coalesce in function)
    null_row = result_df.filter(fn.col("start_date").isNull()).collect()
    if null_row:
        assert null_row[0]["working_days"] == 0, "Null dates should have 0 working days"
    
    print("✅ Null dates handled correctly")


def test_working_days_different_column_name(spark,working_days_calendar):
    """
    Test with a different column name for start date
    """
    # ARRANGE
    data = [("2023-01-01",), ("2023-02-01",)]
    columns = ["month_beginning"]  # Different column name
    input_df = spark.createDataFrame(data, columns)
    
    # ACT
    result_df = working_days_monthly(working_days_calendar, input_df, "month_beginning")
    
    # ASSERT
    assert "working_days" in result_df.columns
    assert result_df.count() == 2
    
    print("✅ Different column name handled correctly")


def test_working_days_values_are_reasonable(working_days_calendar, sample_dataframe_multiple_months):
    """
    Test that all working days values are within reasonable bounds
    No month should have more than 23 working days or less than 19
    """
    # ACT
    result_df = working_days_monthly(working_days_calendar, sample_dataframe_multiple_months, "start_date")
    
    # ASSERT
    results = result_df.collect()
    for row in results:
        working_days = row["working_days"]
        assert 19 <= working_days <= 23, \
            f"Working days should be between 19-23, got {working_days} for {row['start_date']}"
    
    print("✅ All working days values are reasonable")
