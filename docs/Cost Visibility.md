# Cost Visibility

## What you need to do
Todo: how to assign tagging
Todo: add reminder in pull request template
For every notebook, a tag or query? to identify it???  

## Approaches
Todo: table, dashboard, budget tagging, and where triggered, when to pick the tag, what the tage means
budget policys good for, sql would be used for stored procs if we continue using them

## How to view visibility
Todo: link dashboards etc encourage/invite looking at, improvements


# What you dont need to know

## Setup Budget Policys

00_ because defaultest to highest alphabetically. (We should change this to 5 to give head room)
The ```<env>_<costcentre>_<detail>```
Everyone = People

All = People + Sps

I beleive we can use anchors to give these to the dab for the SPs to use rather than having to apply them

Service principle ones will be given via dab and anchors so easy to update. But ones for ppl will need to be ui.
People are given permissions through groups

Other columns are some of the tags will have

qqqq maybe owner names and groups need to become the same. YES

**This approach means you have to apply policies not just have them autoapplied**
**Job tasks need to have policys and tasks need to be seperate enough to have a single policy each not span two**

Unfortunately currently dab is not setting permissions for sps to use the serverless policys so they have to be set through the UI

| Policy Name | Env | CostCentre | Test / Owner | 
|---|---|---|---|
|-------Numbered / General Policies-------| |||
| 00_Dev_Dev_SP_Default | Dev | Dev | SP_Dev |  
| 00_All_All_Phil_Default | All | All  | Person_Phil |  
| 00_Prod_Prod_SP_Default | Prod | Prod | SP_Prod |  
| 00_Staging_Staging_SP_Default | Staging | Staging | SP_Staging  |  
| 01_All_All_PersonAll_Default | All | All | Person_All |  
| All_AdhocAnalysis_All | All | AdhocAnalysis | All  |  
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