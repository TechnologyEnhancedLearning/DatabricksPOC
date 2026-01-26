############
# Based on the isReporter SP
# Will create a table of isReporter instread
# The isReporter will be directly be queeried by site for specific id
# this is to remove sp the idea is to use cdc not recompute per request
# this is so it is faster (unsure currently if it will be but it may)
# DBX should manage its own compute
# i think dlt code is typically a rapper
# i think the python will be the logic (therefore testable)
#########



# reporter_logic.py
from pyspark.sql import functions as F

def compute_is_reporter(users, ual, ugr, uru):
    return (
        users
        .join(ual, users.UserHK == ual.UserHK, "left")
        .join(ugr, users.UserBK == ugr.userId, "left")
        .join(uru, users.UserHK == uru.ReportingUserHK, "left")
        .select(
            users.UserBK.alias("user_id"),
            F.when(
                (F.when(ual.UserHK.isNull(), 0).otherwise(1) +
                 F.when(ugr.userId.isNull(), 0).otherwise(1) +
                 F.when(uru.ReportingUserHK.isNull(), 0).otherwise(1)) == 0,
                0
            ).otherwise(1).alias("is_reporter")
        )
    )