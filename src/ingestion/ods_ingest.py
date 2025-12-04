# for making spark tables
# qqqq problem i am having is that we are setting the schema, and dev has schema set as user names
# i want to use the databricks.yml schema name for dev, and for staging and prod i want to set it to bronze_ods in this script
from pyspark import pipelines as dp


# Fixed System Constants these and some of this stuff should be going in a helper i think
#ADLS_PROTOCOL = "abfss://"
#ADLS_SUFFIX = ".dfs.core.windows.net"

# 1. Get the Catalog name
# qqqq i dont think i want a default id prefer an error i think
# if set this in pipeline yml we wont need it
#catalog_name = spark.conf.get("bundle.catalog")

# 2. Get the Schema Prefix (This is what changes between environments)
# In Dev, this will be the username. In Staging/Prod, it will be blank.
#schema_user_prefix = spark.conf.get("bundle.schema_prefix")
# this will often be a medallion layer but in src we also have transformations and ingestion so i think this mirror folders in source would be logical if team agrees qqqq
#schema_layer = "bronze_"
#schema_domain = "ods" #qqqq check what terminiology we want here

# Construct the final schema name
#schema_name = (schema_user_prefix + schema_layer + schema_domain)
#print(schema_name)
# The container likely should mirror the layer name?
# container_layer ?? qqqq
#container = spark.conf.get("bundle.layer") # layer is bronze silver etc
# This likely should be dev staging prod 
# storage_environment ?? qqqq
# wouldnt have default
# storage_account = spark.conf.get("bundle.storage_account") # 'unifiedrptdeltalake'
storage_container_path = spark.conf.get("pipeline.storage_container_path")
# In our storage our folders maybe should be domain based and if we thing this is manageable as hard rule this variable could be called domain_folder or similar qqqq
# domain_folder ?? qqqq
folder_name = spark.conf.get("pipeline.domain") # ods
#folder_location_path = f"{ADLS_PROTOCOL}{container}@{storage_account}{ADLS_SUFFIX}/{folder_name}/"
folder_location_path = f"{storage_container_path }/{folder_name}/"
# "abfss://bronze@unifiedrptdeltalake.dfs.core.windows.net/ods
print(folder_location_path)


@dp.table(
    # qqqq was f"{schema_name}.Additional_Attributes_Details" but worked before now need to do it this way???!!!
    name="Additional_Attributes_Details",
    comment="Import raw Additional_Attributes_Details"
)
def azure_csv_table():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(
            f"{folder_location_path}Additional_Attributes_Details.csv"
        )
    )

@dp.table(
    name="Code_System_Details",
    comment="Import raw Code_System_Details"
)
def azure_csv_table():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(
            f"{folder_location_path}Code_System_Details.csv"
        )
    ) 

@dp.table(
    name="Contact_Details",
    comment="Import raw Contact_Details"
)
def azure_csv_table():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(
            f"{folder_location_path}Contact_Details.csv"
        )
    ) 

@dp.table(
    name="Manifest_Details",
    comment="Import raw Manifest_Details"
)
def azure_csv_table():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(
            f"{folder_location_path}Manifest_Details.csv"
        )
    ) 

@dp.table(
    name="Organisation_Details",
    comment="Import raw Organisation_Details"
)
def azure_csv_table():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(
            f"{folder_location_path}Organisation_Details.csv"
        )
    ) 

@dp.table(
    name="OtherID_Details",
    comment="Import raw OtherID_Details"
)
def azure_csv_table():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(
            f"{folder_location_path}OtherID_Details.csv"
        )
    ) 

@dp.table(
    name="PrimaryRole_Details",
    comment="Import raw PrimaryRole_Details"
)
def azure_csv_table():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(
            f"{folder_location_path}PrimaryRole_Details.csv"
        )
    ) 

@dp.table(
    name="Relationship_Details",
    comment="Import raw Relationship_Details"
)
def azure_csv_table():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(
            f"{folder_location_path}Relationship_Details.csv"
        )
    )     

@dp.table(
    name="Role_Details",
    comment="Import raw Role_Details"
)
def azure_csv_table():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(
            f"{folder_location_path}Role_Details.csv"
        )
    )

@dp.table(
    name="Successor_Details",
    comment="Import raw Successor_Details"
)
def azure_csv_table():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(
            f"{folder_location_path}Successor_Details.csv"
        )
    )


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