####### THIS CODE IS GENUINCE FROM ANOTHER TEAM IVE JUST MADE SPARK DEPENDENCY INJECTED  ######## 
import os
from pyspark.sql import functions as fn # Added

## def working_days_monthly(df, col_start_date): # Original
## adding spark, and the calendar, so that we seperate concerns and make it testable
## single corncern
## passing in df so dont need to pass spark but often may want to
## def working_days_monthly(spark, df, col_start_date, cal_df):

def working_days_monthly(working_days_cal_df, df, col_start_date):
    """
    Description: Adds a column to monthly level data with working days, based on the first day of the month.
    
    Parameters:
    working_days_cal_df: DI calendar working days
    df: the dataframe to perform the transformation on 
    col_start_date: the column that contains the first date of the month in your dataframe
    
    Returns:
    output: the initial dataframe with the new column added with working days for the month
    """

    # Convert start date in df to date format for comparison
    df = df.withColumn(col_start_date, fn.to_date(fn.col(col_start_date).cast("date")))
    
    # Create a new column with the total working days
    output = df.join(
        working_days_cal_df.select("Month_Start", "Total_Working_Days"),
        fn.col(col_start_date) == fn.col("Month_Start"),
        "left"
    ).withColumn(
        "working_days",
        fn.coalesce(fn.col("Total_Working_Days"), fn.lit(0))
    ).drop("Month_Start", "Total_Working_Days")
    
    return output


############### keeping just because poc
    # ## Added because i dont have the global file
    # calendar_full = "/tmp/standard_calendar.parquet"

    # # 1. RELIABLE CHECK: Does the file exist?
    # file_exists = False
    # try:
    #     dbutils.fs.ls(calendar_full)
    #     file_exists = True
    # except:
    #     file_exists = False

    # # 2. GENERATE if missing
    # if not file_exists:
    #     print(f"Creating missing calendar at {calendar_full}...")
    #     spark.range(0, 365 * 10).select(
    #         fn.expr("date_add('2020-01-01', cast(id as int))").alias("Date")
    #     ).withColumn("Month_Start", fn.trunc("Date", "MM")) \
    #      .withColumn("Working_Day_Type", fn.when(fn.date_format("Date", "EEEE").isin("Saturday", "Sunday"), "N").otherwise("Y")) \
    #      .withColumn("Working_Day_Calc", fn.when(fn.col("Working_Day_Type") == "Y", 1).otherwise(0)) \
    #      .write.mode("overwrite").parquet(calendar_full)

    # # 3. READ (This will now definitely work)
    # cal_df = spark.read.parquet(calendar_full)   # This is a global file i dont have

        # working_days_cal_df = working_days_cal_df.filter(fn.col("Working_Day_Type") == "Y").dropDuplicates()

    # working_days_cal_df = working_days_cal_df.withColumn(
    #     "Month_Start",
    #     fn.date_format(fn.to_date(fn.col("Month_Start"), "yyyy-MM-dd"), "yyyy-MM-dd").cast("date")
    # )

    # Aggregate by Month_Start and sum Working_Day_Calc
    # working_days_cal_df = working_days_cal_df.groupBy(
    #     "Month_Start"
    # ).agg(
    #     fn.sum("Working_Day_Calc").alias("Total_Working_Days")
    # )