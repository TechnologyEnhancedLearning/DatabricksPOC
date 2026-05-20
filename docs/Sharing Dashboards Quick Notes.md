# Dashboards for External Users Quick Notes
**Needs a thorough exploration this has just been checking for functionality**
- sharepoint sharing option with SSO
- external option with api, obviously compute cost to ppl accessing it (though maybe we wouldnt make it dynamicaly get data)
	- we could put cost controls on individual dashboards or all of them by the looks
- previously ive been concerned of giving access to databricks but it i think does have options that are safe where you only see "published dashboards" as an "external user"
	- i would very much want to do this with groups etc
- can have user refresh or periodic
- Databricks view-only users (users who have been added to the Databricks account, but not to any workspace)
- Publishing creates a snapshot of the current configuration, so when it is shared, viewers will see this polished version instead of any ongoing edits.
- Without credential embedding, viewers will use their own credentials, which is necessary if you want to personalize content based on the user or maintain strict data access controls (e.g. as declared in Unity Catalog). ... with is just they can use it and it uses our resource automatically
- we would want to restrict the dashboards to only have permissions to the tables it should, i think though this is mainly an extra precaution - will need checking it may be a matter of course
- Sharing with individual users or groups: You can find them in the sharing dialog's search results.
- Sharing with the whole organization: You can set the dashboard to "Anyone in my organization can view."

- Admins can do this in several ways:

Manually add users or groups to the Databricks account and simply do not grant them workspace access to keep them view-only. (docs)
Use the Databricks User APIs to programmatically manage user access. (docs)
Use SCIM to sync users and groups from Entra IDOkta, or another identity provider. (docs)
Directly use Seamless sharing for Entra ID users and groups in Databricks (currently in private preview, talk with your account representative for access).
Just-in-time account user provisioning (currently in private preview, talk with your account representative for access), which automatically adds users to the Databricks account when they log in through your identity provider.

# Refs
https://learn.microsoft.com/en-gb/azure/databricks/dashboards/share/embedding/#embedding-for-external-users

"Service principal’s permissions control API access, but shared data permissions (if granted) still determine data access"

https://learn.microsoft.com/en-gb/azure/databricks/dashboards/share/embedding/external-embed
- this has a diagram of token between databricks and your space

https://www.databricks.com/blog/sharing-aibi-dashboards
- view only databricks users


[not watched but probably a useful demonstration youtube](https://www.databricks.com/aibi-intelligent-analytics-real-world-data?itm_data=demo_center)
[looks like a useful how to video on adding and sending an email to external users](https://youtu.be/fbTstFmAdAs)