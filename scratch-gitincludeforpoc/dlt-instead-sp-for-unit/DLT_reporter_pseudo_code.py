# This is a wrapper the logic is in reporter_logic
# its just ai generated for context
# it would use the logic create a delta live table the table would be updated via cdc
# website would use read only on the table no compute or complex query logic
# the report_logic should be testable
# the pipeline would provide catalog schema etc see ingest example


# pipelines/dlt_reporter_pipeline.py
import dlt
from pyspark.sql import functions as F
# named by the init file compute_is_reporter
from src.reporter_logic import compute_is_reporter

@dlt.table(name="user_reporter_status")
def user_reporter_status():
    """Compute reporter status."""
    
    # Use dlt.read() for tables in the same DLT pipeline
    users = (
        dlt.read("user")  # Reads from your DLT pipeline
        .filter(F.col("UserDeleted") == 'false')
    )
    
    ual = (
        dlt.read("useradminlocation")
        .filter(F.col("Deleted") == 'false')
        .filter(~F.col("LocationBK").isin([1, 190822]))
    )
    
    ugr = (
        dlt.read("usergroupreportertbl")
        .filter(F.col("deleted") == False)
    )
    
    uru = (
        dlt.read("userreportinguser")
        .filter(F.col("Deleted") == 'false')
    )
    
    return compute_is_reporter(users, ual, ugr, uru)