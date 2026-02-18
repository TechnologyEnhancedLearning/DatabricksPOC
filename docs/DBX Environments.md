# Environments

## DBX Environment Features
Bundle/Pipeline Development Mode: Pause cron jobs, streaming, uses cheaper resources?, leave clusters active longer.

⚠️Because pipelines are triggered by jobs that may not be automatically trigger in dev, when writing new pipelines you will need to run them manually to see tables created, and then test their data. The do not run as part of the bundle deploy. 

### Personal
- your user space
- for the feature your working on
- related to your feature branch
- others have view access
- development mode so no streaming
- deployed manually via ui
- no cron jobs so pipelines manually triggered dev
- data for this environment is in catalog dev, then your username for schema

### Dev
- Space for analysts work to combine
- pr is required to merge in a feature this should all be working code
- is a dab deployed version of dev branch
- deployed by cicd
- Dev mode so no streaming
- joint space should be manage by service prinicple

### Staging
- space for analysts and testers
- is a dab deployed version of staging branch
- production ready code is here
- it is in prod mode
- managed by service principle

### Prod
- is a dab deployed version of main branch
- light version of dab deployed here