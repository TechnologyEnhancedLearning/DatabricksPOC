#### none of first 1000 are a reporter unsure if broken

######

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

import dlt
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Get spark session for reading external tables
#spark = SparkSession.builder.getOrCreate()

from reporter_logic import compute_is_reporter



# Silver: Computed is_reporter table (FAKE LIVE TABLE)
@dlt.table(
    name="user_reporter_status",
    comment="FAKE Live table showing which users are reporters (would be if streaming tables were in poc)",
    table_properties={
        "quality": "silver",
        "layer": "silver"
    }
)
# this is not streaming but it would be if it was the same workspace so intead spark.read. is used rather than dlt.read_stream
def is_reporter_silver():

    # Fully qualify with catalog name
    # we would specify the catalog as we would use the dab or pipeline value for this but for the scope of the poc we will just read from where we have data currently
    external_catalog_for_expedience = "uks_tel_databricks_dev_3560006266579683"

    # Read from your existing bronze tables
    """
    Computes reporter status for all users based on:
    - Location-based permissions (useradminlocation)
    - User group permissions (usergroupreporter) 
    - Direct user permissions (userreportinguser)
    
    TODO: Consider moving to gold_reporting layer as this is cross-domain aggregation
    """
    # we would do all logic in one pipeline or have the dependent tables cdc too i expect but for the scope of the poc we will just read
    users = (spark.read.table(f"{external_catalog_for_expedience}.bronze_learning_hub.hub_user").filter(~F.col("Deleted")))
    
    ual = (spark.read.table(f"{external_catalog_for_expedience}.bronze_learning_hub.elfh_useradminlocationtbl")
           .filter(~F.col("Deleted") & ~F.col("adminLocationId").isin([1, 190822])))
    
    ugr = (spark.read.table(f"{external_catalog_for_expedience}.bronze_learning_hub.elfh_usergroupreportertbl").filter(~F.col("deleted")))
    
    uru = (spark.read.table(f"{external_catalog_for_expedience}.bronze_learning_hub.elfh_userreportingusertbl").filter(~F.col("Deleted")))
    
    # Use your existing logic
    return compute_is_reporter(users, ual, ugr, uru)


# def is_reporter_silver_streaming_doesnt_work_only_beause_seperate_workspace():

#     # Fully qualify with catalog name
#     # we would specify the catalog as we would use the dab or pipeline value for this but for the scope of the poc we will just read from where we have data currently
#     external_catalog_for_expedience = "uks_tel_databricks_dev_3560006266579683"

#     # Read from pre existing tables they are already streaming by cdc so dont need to join by cdc as its an ingestion process
#     """
#     Computes reporter status for all users based on:
#     - Location-based permissions (useradminlocation)
#     - User group permissions (usergroupreporter) 
#     - Direct user permissions (userreportinguser)
    
#     TODO: Consider moving to gold_reporting layer as this is cross-domain aggregation
#     """
#     # we would do all logic in one pipeline or have the dependent tables cdc too i expect but for the scope of the poc we will just read
#     users = (dlt.read(f"{external_catalog_for_expedience}.bronze_learning_hub.hub_user").filter(~F.col("Deleted")))
    
#     ual = (dlt.read(f"{external_catalog_for_expedience}.bronze_learning_hub.elfh_useradminlocationtbl")
#            .filter(~F.col("Deleted") & ~F.col("adminLocationId").isin([1, 190822])))
    
#     ugr = (dlt.read(f"{external_catalog_for_expedience}.bronze_learning_hub.elfh_usergroupreportertbl").filter(~F.col("deleted")))
    
#     uru = (dlt.read(f"{external_catalog_for_expedience}.bronze_learning_hub.elfh_userreportingusertbl").filter(~F.col("Deleted")))
    
#     # Use your existing logic
#     return compute_is_reporter(users, ual, ugr, uru)


# def is_reporter_silver_cdc_logic_not_needed_these_are_streaming_tbls():

#     ##  elfh_userreportingusertbl - > elfh_userreportingusertbl_ct is streaming
#     ##  elfh_useradminlocationtbl - > no ct table is streaming
#     ##  elfh_usergroupreportertbl -> no ct table  is streaming
#     ##  hub_user -> hub_user_ct is streaming
#     ##
#     ## Will join such that only ct changes result in results returning this means the POC isnt truly live, we would actually want to track all of them, but this shows the approach

#     # Incremental processing triggered by CT tables:
#     # ✓ hub_user_ct - drives incremental updates
#     # ✓ userreportinguser_ct - drives incremental updates
#     # not all the tables because just poc

#     # Fully qualify with catalog name
#     # we would specify the catalog as we would use the dab or pipeline value for this but for the scope of the poc we will just read from where we have data currently
#     external_catalog_for_expedience = "uks_tel_databricks_dev_3560006266579683"

#     # Read from your existing bronze tables
#     """
#     Computes reporter status for all users based on:
#     - Location-based permissions (useradminlocation)
#     - User group permissions (usergroupreporter) 
#     - Direct user permissions (userreportinguser)
    
#     TODO: Consider moving to gold_reporting layer as this is cross-domain aggregation
#     """

#     # Stream from CT tables - this drives the incremental processing
#     user_changes = dlt.read_stream(f"{external_catalog_for_expedience}.learninghub_catalog.cdc.hub_user_ct")

#     uru_changes = dlt.read_stream(f"{external_catalog_for_expedience}.learninghub_catalog.cdc.elfh_userreportingusertbl_ct")

#     # Join CT streams to main tables to get full records
#     users = (
#         user_changes
#         .join(
#             dlt.read(f"{external_catalog_for_expedience}.bronze_learning_hub.hub_user"),
#             "Id == UserId"  # adjust to your actual PK column
#         )
#         .filter(~F.col("Deleted"))
#     )

#     uru = (
#         uru_changes
#         .join(
#             dlt.read(f"{external_catalog_for_expedience}.bronze_learning_hub.elfh_userreportingusertbl"),
#             "userReportingUserId"  # adjust to your actual PK column
#         )
#         .filter(~F.col("Deleted"))
#     )
    

    
#     # These will be read in full whenever the CT tables trigger an update   
#     # Changes to ONLY these tables won't trigger a refresh (acceptable for POC)
#     ual = (
#         dlt.read(f"{external_catalog_for_expedience}.bronze_learning_hub.elfh_useradminlocationtbl")
#         .filter(~F.col("Deleted") & ~F.col("adminLocationId").isin([1, 190822]))
#     )
    
#     ugr = (
#         dlt.read(f"{external_catalog_for_expedience}.bronze_learning_hub.elfh_usergroupreportertbl")
#         .filter(~F.col("deleted"))
#     )
    
#     uru = (
#         uru_changes
#         .join(
#             dlt.read(f"{external_catalog_for_expedience}.bronze_learning_hub.elfh_userreportingusertbl"),
#             "userReportingUserId"  # unsure if is PK
#         )
#         .filter(~F.col("Deleted"))
#     )
    
#     # Use your existing logic
#     return compute_is_reporter(users, ual, ugr, uru)

# def is_reporter_silver_works_but_inofficient_full_table():

#     # Fully qualify with catalog name
#     # we would specify the catalog as we would use the dab or pipeline value for this but for the scope of the poc we will just read from where we have data currently
#     external_catalog_for_expedience = "uks_tel_databricks_dev_3560006266579683"

#     # Read from your existing bronze tables
#     """
#     Computes reporter status for all users based on:
#     - Location-based permissions (useradminlocation)
#     - User group permissions (usergroupreporter) 
#     - Direct user permissions (userreportinguser)
    
#     TODO: Consider moving to gold_reporting layer as this is cross-domain aggregation
#     """
#     # we would do all logic in one pipeline or have the dependent tables cdc too i expect but for the scope of the poc we will just read
#     users = (spark.read.table(f"{external_catalog_for_expedience}.bronze_learning_hub.hub_user").filter(~F.col("Deleted")))
    
#     ual = (spark.read.table(f"{external_catalog_for_expedience}.bronze_learning_hub.elfh_useradminlocationtbl")
#            .filter(~F.col("Deleted") & ~F.col("adminLocationId").isin([1, 190822])))
    
#     ugr = (spark.read.table(f"{external_catalog_for_expedience}.bronze_learning_hub.elfh_usergroupreportertbl").filter(~F.col("deleted")))
    
#     uru = (spark.read.table(f"{external_catalog_for_expedience}.bronze_learning_hub.elfh_userreportingusertbl").filter(~F.col("Deleted")))
    
#     # Use your existing logic
#     return compute_is_reporter(users, ual, ugr, uru)