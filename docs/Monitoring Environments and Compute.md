# Monitoring Environments

- Post Deployment check in PR template

## Planned Process

- Email address per environment
- Dashboard per environment
- Git Actions per environment
- Run tests on deploy (excluding prod)

### Future

Azure Monitor and Azure Log Analytics to implement webhooks to teams channels
[Microsoft learn DBX azure log streaming](https://learn.microsoft.com/en-us/training/wwl-databricks/monitor-troubleshoot-optimize-workloads-azure-databricks/6-implement-log-streaming-azure-analytics)
- provides opportunity to link other logs (e.g. LH, DBs) and therefore correlate issues

## Compute

Serverless is for now our best choice.
Spot instance pool clusters around an executor node, may be more cost efficient for dev staging potentially
**Cluster give us more granularity but more management overhead
Serverless Warehouse SQL may be better than general serverless for reading gold but where work 
is done e.g. python serverless compute is best**

[compute chosing dbx microsoft course](https://learn.microsoft.com/en-us/training/wwl-databricks/select-and-configure-compute/4-configure-compute-feature-settings)
  - has useful flowcharts through out for making compute choices