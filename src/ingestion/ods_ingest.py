
# worked but improving pathing
# unless we set up a wheel artifact this is required to access utils
import sys
import os
sys.path.append(os.path.abspath('..'))


from pyspark import pipelines as dp
from utils.loaders import load_csv_table

# storage_account = spark.conf.get("bundle.storage_account") # 'unifiedrptdeltalake'
storage_container_path = spark.conf.get("pipeline.storage_container_path")
folder_name = spark.conf.get("pipeline.domain") # ods
folder_location_path = f"{storage_container_path}/{folder_name}/"

print(folder_location_path)


# List of table names
TABLE_NAMES = [
    "Additional_Attributes_Details",
    "Code_System_Details",
    "Contact_Details",
    "Manifest_Details",
    "Organisation_Details",
    "OtherID_Details",
    "PrimaryRole_Details",
    "Relationship_Details",
    "Role_Details",
    "Successor_Details",
]


# Define all ODS tables with their configurations
# tables as keys because unique
# only using dictionary because expect future use to have more to it

# Generate table configurations dynamically
ODS_TABLES = {
    table_name: {
        "csv_filename": f"{table_name}.csv",
        "comment": f"Import raw {table_name}"
    }
    for table_name in TABLE_NAMES
}
# ALternatively if need to set the values specifically
# ODS_TABLES = {
#     "Additional_Attributes_Details": {
#         "csv_filename": "Additional_Attributes_Details.csv",
#         "comment": "Import raw Additional_Attributes_Details"
#     },
#     "Code_System_Details": {
#         "csv_filename": "Code_System_Details.csv",
#         "comment": "Import raw Code_System_Details"
#     } ....
#


# Create DLT tables dynamically
for table_name, config in ODS_TABLES.items():
    # Create a closure to capture the current loop variables
    def create_table(name=table_name, cfg=config):
        @dp.table(name=name, comment=cfg["comment"])
        def table_loader():
            # spark is defined by databricks environment its provided globally here but as load_csv_table is the unit testable part we make it a passable argument
            return load_csv_table( spark, folder_location_path, cfg["csv_filename"])
        return table_loader
    
    create_table()


#######################################################################
### DEL just keeping because poc
##########################################################


# def load_csv_table(table_name):
#     """Load CSV from Azure storage with standard options"""
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(f"{folder_location_path}{table_name}.csv")
#     )

# # Create DLT tables dynamically
# for table_name, comment in ODS_TABLES:
#     # Create a closure to capture the current loop variables
#     def create_table(name=table_name, desc=comment):
#         @dp.table(name=name, comment=desc)
#         def table_loader():
#             return load_csv_table(name)
#         return table_loader
    
#     create_table()

# @dp.table(
#     # qqqq was f"{schema_name}.Additional_Attributes_Details" but worked before now need to do it this way???!!!
#     name="Additional_Attributes_Details",
#     comment="Import raw Additional_Attributes_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"{folder_location_path}Additional_Attributes_Details.csv"
#         )
#     )

# @dp.table(
#     name="Code_System_Details",
#     comment="Import raw Code_System_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"{folder_location_path}Code_System_Details.csv"
#         )
#     ) 

# @dp.table(
#     name="Contact_Details",
#     comment="Import raw Contact_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"{folder_location_path}Contact_Details.csv"
#         )
#     ) 

# @dp.table(
#     name="Manifest_Details",
#     comment="Import raw Manifest_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"{folder_location_path}Manifest_Details.csv"
#         )
#     ) 

# @dp.table(
#     name="Organisation_Details",
#     comment="Import raw Organisation_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"{folder_location_path}Organisation_Details.csv"
#         )
#     ) 

# @dp.table(
#     name="OtherID_Details",
#     comment="Import raw OtherID_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"{folder_location_path}OtherID_Details.csv"
#         )
#     ) 

# @dp.table(
#     name="PrimaryRole_Details",
#     comment="Import raw PrimaryRole_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"{folder_location_path}PrimaryRole_Details.csv"
#         )
#     ) 

# @dp.table(
#     name="Relationship_Details",
#     comment="Import raw Relationship_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"{folder_location_path}Relationship_Details.csv"
#         )
#     )     

# @dp.table(
#     name="Role_Details",
#     comment="Import raw Role_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"{folder_location_path}Role_Details.csv"
#         )
#     )

# @dp.table(
#     name="Successor_Details",
#     comment="Import raw Successor_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"{folder_location_path}Successor_Details.csv"
#         )
#     )


###### Try this
# import dlt
# from pyspark.sql import SparkSession

# # ============================================================================
# # Configuration from Bundle
# # ============================================================================
# storage_account = spark.conf.get("bundle.storage_account")
# layer = spark.conf.get("bundle.layer")  # "bronze"
# domain = spark.conf.get("bundle.domain")  # "ods"

# # ============================================================================
# # Constants
# # ============================================================================
# ADLS_PROTOCOL = "abfss://"
# ADLS_SUFFIX = ".dfs.core.windows.net"

# # ============================================================================
# # Derived Paths
# # ============================================================================
# container = layer  # Container matches layer
# folder_path = f"{ADLS_PROTOCOL}{container}@{storage_account}{ADLS_SUFFIX}/{domain}/"

# # ============================================================================
# # Data Model - ODS Tables
# # ============================================================================
# ODS_TABLES = [
#     ("Additional_Attributes_Details", "Import raw Additional_Attributes_Details"),
#     ("Code_System_Details", "Import raw Code_System_Details"),
#     ("Contact_Details", "Import raw Contact_Details"),
#     ("Manifest_Details", "Import raw Manifest_Details"),
#     ("Organisation_Details", "Import raw Organisation_Details"),
#     ("OtherID_Details", "Import raw OtherID_Details"),
#     ("PrimaryRole_Details", "Import raw PrimaryRole_Details"),
#     ("Relationship_Details", "Import raw Relationship_Details"),
#     ("Role_Details", "Import raw Role_Details"),
#     ("Successor_Details", "Import raw Successor_Details"),
# ]

# # ============================================================================
# # Helper Functions <----- this is what would go in a wheel probably
# # ============================================================================
# def load_csv(filename: str):
#     """Load CSV from Azure storage with standard options"""
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(f"{folder_path}{filename}.csv")
#     )

# # ============================================================================
# # Create DLT Tables
# # ============================================================================
# for table_name, comment in ODS_TABLES:
#     # Closure to capture loop variables correctly
#     def create_table(name=table_name, desc=comment):
#         @dlt.table(name=name, comment=desc)
#         def table_loader():
#             return load_csv(name)
#         return table_loader
    
#     create_table()