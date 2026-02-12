"""Data loading utilities for Databricks pipelines"""
# spark is injectable so we can do testing
# the function should do only one thing so it can be testable
def load_csv_table(spark, base_path, csv_filename):
    """Load CSV from Azure storage with standard options
    
    Args:
        base_path: Base path to the folder containing CSV files
        csv_filename: Name of the CSV file to load
        
    Returns:
        DataFrame: Spark DataFrame with CSV data
    """
    import os
    full_path = os.path.join(base_path, csv_filename)
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(full_path)
    )