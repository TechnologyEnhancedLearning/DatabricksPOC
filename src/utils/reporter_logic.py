############
# Based on the isReporter SP
# Will create a table of isReporter instread
# The isReporter will be directly be queeried by site for specific id
# this is to remove sp the idea is to use cdc not recompute per request
# this is so it is faster (unsure currently if it will be but it may)
# DBX should manage its own compute
# i think dlt code is typically a rapper
# i think the python will be the logic (therefore testable)
# see dlt-instead-sp-for-unit folder in scratch
#########



# reporter_logic.py
from pyspark.sql import functions as F

def compute_is_reporter(users, ual, ugr, uru):
    return (
         users
        # Join on AU.Id = UAL.userId
        .join(ual, users.Id == ual.userId, "left")
        # Join on UGR.userId = AU.Id
        .join(ugr, ugr.userId == users.Id, "left")
        # Join on URU.reportingUserId = AU.Id
        .join(uru, uru.reportingUserId == users.Id, "left")
        .select(
            users.Id.alias("user_id"),
            # Match the CASE WHEN logic from SQL
            F.when(
                (F.when(ual.userId.isNull(), 0).otherwise(1) +
                 F.when(ugr.userId.isNull(), 0).otherwise(1) +
                 F.when(uru.reportingUserId.isNull(), 0).otherwise(1)) == 0,
                0
            ).otherwise(1).alias("is_reporter")
        )
        .distinct()  # DISTINCT from original SQL
        # users
        # .join(ual, users.UserHK == ual.UserHK, "left")
        # .join(ugr, users.UserBK == ugr.userId, "left")
        # .join(uru, users.UserHK == uru.ReportingUserHK, "left")
        # .select(
        #     users.UserBK.alias("user_id"),
        #     F.when(
        #         (F.when(ual.UserHK.isNull(), 0).otherwise(1) +
        #          F.when(ugr.userId.isNull(), 0).otherwise(1) +
        #          F.when(uru.ReportingUserHK.isNull(), 0).otherwise(1)) == 0,
        #         0
        #     ).otherwise(1).alias("is_reporter")
        # )
    )