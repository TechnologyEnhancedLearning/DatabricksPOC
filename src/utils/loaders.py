"""Data loading utilities for Databricks pipelines"""
# i dont think we will want these as a package just as a module we wont be expoting and its just and extra steps for analyst which currently i do not think will provide value until they request it and will get in their way
def load_csv_table(spark, base_path, csv_filename):
    """Load CSV from Azure storage with standard options
    
    Args:
        base_path: Base path to the folder containing CSV files
        csv_filename: Name of the CSV file to load
        
    Returns:
        DataFrame: Spark DataFrame with CSV data
    """
    
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(f"{base_path}{csv_filename}")
    )