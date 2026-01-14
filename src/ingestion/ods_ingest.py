import sys
from pathlib import Path

########### qqqq previous approach worked but not with git etc #####
## this worked but suspicious of it in dabs staging github etc
#import os
# sys.path.append(os.path.abspath('..')) 
#  with utils.loaders from loaders import load_csv_table 
# and the init was from .loaders import load_csv_table  __all__ = ["load_csv_table"]
# # from utils.loaders import load_csv_table  # worked
##############


############### Make Modules Available  #############
current_dir = Path.cwd()
print(f"Current_dir: {current_dir}")
shared_parent_root = current_dir.parent.resolve()
print(f"shared_parent_root: {shared_parent_root}")
module_folder_path_from_shared_parent = "utils"
module_path = (shared_parent_root / module_folder_path_from_shared_parent).resolve()
print(f"module_path: {module_path}")
if str(module_path) not in sys.path:
    sys.path.insert(0, str(module_path))
######################################################

from pyspark import pipelines as dp
from loaders import * #load_csv_table


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