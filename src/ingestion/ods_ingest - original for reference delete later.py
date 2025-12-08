# from pyspark import pipelines as dp

# container = 'bronze'
# storage_account = 'unifiedrptdeltalake'
# path_to_file_or_folder = 'ods'

# @dp.table(
#     name="bronze_ods.Additional_Attributes_Details",
#     comment="Import raw Additional_Attributes_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"abfss://{container}@{storage_account}.dfs.core.windows.net/{path_to_file_or_folder}/Additional_Attributes_Details.csv"
#         )
#     )

# @dp.table(
#     name="bronze_ods.Code_System_Details",
#     comment="Import raw Code_System_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"abfss://{container}@{storage_account}.dfs.core.windows.net/{path_to_file_or_folder}/Code_System_Details.csv"
#         )
#     ) 

# @dp.table(
#     name="bronze_ods.Contact_Details",
#     comment="Import raw Contact_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"abfss://{container}@{storage_account}.dfs.core.windows.net/{path_to_file_or_folder}/Contact_Details.csv"
#         )
#     ) 

# @dp.table(
#     name="bronze_ods.Manifest_Details",
#     comment="Import raw Manifest_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"abfss://{container}@{storage_account}.dfs.core.windows.net/{path_to_file_or_folder}/Manifest_Details.csv"
#         )
#     ) 

# @dp.table(
#     name="bronze_ods.Organisation_Details",
#     comment="Import raw Organisation_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"abfss://{container}@{storage_account}.dfs.core.windows.net/{path_to_file_or_folder}/Organisation_Details.csv"
#         )
#     ) 

# @dp.table(
#     name="bronze_ods.OtherID_Details",
#     comment="Import raw OtherID_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"abfss://{container}@{storage_account}.dfs.core.windows.net/{path_to_file_or_folder}/OtherID_Details.csv"
#         )
#     ) 

# @dp.table(
#     name="bronze_ods.PrimaryRole_Details",
#     comment="Import raw PrimaryRole_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"abfss://{container}@{storage_account}.dfs.core.windows.net/{path_to_file_or_folder}/PrimaryRole_Details.csv"
#         )
#     ) 

# @dp.table(
#     name="bronze_ods.Relationship_Details",
#     comment="Import raw Relationship_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"abfss://{container}@{storage_account}.dfs.core.windows.net/{path_to_file_or_folder}/Relationship_Details.csv"
#         )
#     )     

# @dp.table(
#     name="bronze_ods.Role_Details",
#     comment="Import raw Role_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"abfss://{container}@{storage_account}.dfs.core.windows.net/{path_to_file_or_folder}/Role_Details.csv"
#         )
#     )

# @dp.table(
#     name="bronze_ods.Successor_Details",
#     comment="Import raw Successor_Details"
# )
# def azure_csv_table():
#     return (
#         spark.read.format("csv")
#         .option("header", "true")
#         .option("inferSchema", "true")
#         .load(
#             f"abfss://{container}@{storage_account}.dfs.core.windows.net/{path_to_file_or_folder}/Successor_Details.csv"
#         )
#     )