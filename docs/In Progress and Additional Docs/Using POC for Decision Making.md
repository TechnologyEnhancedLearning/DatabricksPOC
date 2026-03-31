# Using Poc For Decison Making

## Feature not included
- Pull request doc
- Versioning <- recommend manual
- multi environments (uses catalogs for poc)
- doc how to write tests



## Features
What will we use? 
how much will we use it?
does anything else need exploring?
should some be adopted no into DBX so we can get in the habit?
best way to support it being used?
- small tasks to implement so it is explored

DAB
Unit, Integration, Data, (and slight example reporting)
Git Deployed Test
Lint
File structure

## Not our set up but close so useful for some context
![Azure Databricks Bundles CI/CD](https://learn.microsoft.com/en-gb/azure/databricks/_static/images/bundles/bundles-cicd.png)
## Discussion
- pros and cons of environments
  - does mean 3x setup but not big deal
  - the metastore same so cost isnt increased
  - prod not impacted
  - seperate costs so smallr cluster dev
  - view permissions staging prod, development in dev
  - dab lighter for prod
- how many environments do we need see deployment_guide
  [ui retrival of existing pipleine](https://learn.microsoft.com/en-gb/azure/databricks/dev-tools/bundles/migrate-resources#existing-pipeline)
  [blog contributor](https://community.databricks.com/t5/administration-architecture/what-is-best-practice-for-determining-how-many-workspaces-i-need/m-p/44760#M395)
  [matches our approach dbx bundle architecture](https://learn.microsoft.com/en-gb/azure/databricks/dev-tools/bundles/)
  [blog dbx](https://www.databricks.com/blog/2022/03/10/functional-workspace-organization-on-databricks.html)
  [3 vertical dots actually visible yml for pipelines](https://adb-3560006266579683.3.azuredatabricks.net/jobs/944561798154284/code?o=3560006266579683)
    - nice quote "implement strict guidelines before beginning to onramp workloads to your Lakehouse; in other words, measure twice, cut once!"
    - 
  - prod definately seperate
  - staging, dev, personal ???
    - any requirement gov
    - would tester read access work? then can combine dev-staging
      - for
        - simpler in that dev = analyst, staging = test, prod = prod
        - simpler seperate cost (can still do with sps and named clusters) dev not streaming as does not support a staging lh, dev is experimental space, and has less requirements
        - easier seeing those costs
        - dev would be changeable without interfering with tests
      - against 
        - seperating by catalog and service principles is doable
        - maybe easier to setup but still need sps etc

- why dabs
  - simple automated deployment across environments with advantages of git backbone
- thoughts on naming, can J provide domain names etc if its a good idea

  