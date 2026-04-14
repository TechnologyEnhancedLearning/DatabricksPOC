# Tags and Policy Budgets

Tags and cost visibility go together in this document. This is because the budget policys allow us to track serverless costs, and tags allow us to sort pipelines and jobs in the databricks UI amongst other things. 

Having tags set in the tags section, and tags in serverless budget policys could get confusing. So serverless budget policys should be for every job, pipeline and notebook, tags should be occassionaly applied where different or more granuality is required.

The severless budget policys override the tags set in jobs  and pipelines for budget tables (where they match), and allow us to capture serverless costs. 

Tags set in the tag section are nice because the UI use them and not the policy set ones currently.

##  Policy and Tags Reference

⚠️ This is the first thought for budget policy strategy this is worth some thought: Should we track data coming in/out, who is consuming it, batch or live consumed, etc.

*Maybe we should have tags in Staging_Analysis_Batch for ingestion or medallion, but until we have some good queries and dashboards we wont know what the most useful tags are*

Policy naming 
```<number (if you want it to default to a certain order)>-<Env>-<CostCentre>-<Test or Owner (which ever most useful to know)>``` 
you may add DEFAULT on the end it is a policy to fallback on when one isnt assigned.


| Policy Name | Env | CostCentre | Test / Owner | 
|---|---|---|---|
|-------Numbered / General Policies-------| |||
| 00_Dev_Dev_SP_Default | Dev | Dev | SP_Dev |  
| 00_All_All_Phil_Default | All | All  | Person_Phil |  
| 00_Prod_Prod_SP_Default | Prod | Prod | SP_Prod |  
| 00_Staging_Staging_SP_Default | Staging | Staging | SP_Staging  |  
| 01_All_All_PersonAll_Default | All | All | Person_All |  
| All_AdhocAnalysis_All | All | AdhocAnalysis | All  |  
|-------Personal Policies-------| |||
| Personal_Test_All | Personal | Test | All |  |
|-------Staging Policies-------| |||
| Staging_Analysis_Batch | Staging | Analysis |  |  |
| Staging_LH_Live | Staging | LH |  |  |
| Staging_Test_All | Staging | Test | All |  |
| Staging_Test_DQ | Staging | Test | DQ |  |
| Staging_Test_Int | Staging | Test | Int |  |
| Staging_Test_Unit | Staging | Test | Unit |  |
|-------Prod Policies-------| |||
| Prod_Analysis_Batch | Prod | Analysis |  |  |
| Prod_LH_Live | Prod | LH |  |  |
|-------Dev Policies-------| |||
| Dev_Analysis_Batch | Dev | Analysis |  |  |
| Dev_LH_Live | Dev | LH |  |  |
| Dev_Test_All | Dev | Test | All |  |
| Dev_Test_DQ | Dev | Test | DQ |  |
| Dev_Test_Int | Dev | Test | Int |  |
| Dev_Test_Unit | Dev | Test | Unit |  |




## Cost Visibility

### What you need to do
Todo: how to assign tagging
Todo: add reminder in pull request template
For every notebook, a tag or query? to identify it???  
Drop down databricks instances, settings, to usage is how to connect the policyies to azure

### Approaches
Todo: table, dashboard, budget tagging, and where triggered, when to pick the tag, what the tage means
budget policys good for, sql would be used for stored procs if we continue using them

### How to view visibility
Todo: link dashboards etc encourage/invite looking at, improvements

# FYI
[budget policies limitations and delay](https://learn.microsoft.com/en-us/azure/databricks/admin/usage/budget-policies)
- Updates to tags won't be reflected in new pipeline updates if the pipeline is in Development mode. The changes take 24 hours to propagate.
- Pipelines triggered by jobs do not inherit the job's serverless budget policy. Users must set the pipeline's policy.

# What you dont need to know

## Azure
- Budgets minimum gradularity is 1 month

## Budget calculation limitations
[Microsoft link serverless budgets](https://learn.microsoft.com/en-us/azure/databricks/admin/account-settings/budgets#known-limitations)
> Budgets do not factor in any billing credits or negotiated discounts your account might have. The spent amount is calculated by multiplying usage by the SKU list price.

## Setup Budget Policys

00_ because defaultest to highest alphabetically. (We should change this to 5 to give head room)
The ```<env>_<costcentre>_<detail>```
Everyone = People

All = People + Sps

I beleive we can use anchors to give these to the dab for the SPs to use rather than having to apply them

Service principle budget policies will be given via dab and anchors so easy to update. But ones for ppl will need to be ui.
People are given permissions to use policies through groups. They apply policies to notebooks etc by clicking the vertical slider symbol on the right and setting policy. (When making jobs and pipelines, policy and tags should be defined and match each other)

Other columns are some of the tags will have

**This approach means you have to apply policies not just have them autoapplied**
**Job tasks need to have policys and tasks need to be seperate enough to have a single policy each not span two**

Unfortunately currently dab is not setting permissions for sps to use the serverless policys so they have to be set through the UI.
