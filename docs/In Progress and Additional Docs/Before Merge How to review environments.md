# Todo
This file will be for J with input from the team on what should be part of it.
- A pr proformer specific to pulling into environment branches would be more consistent or convenient if possible ... otherwise add environment sections to existing one?

# Dev
- in prs include instructions on what needs checking after dev deployment,
we want some process to identify easily what task went into dev, and collect any recommendations in those tasks for dev checks, to inform checking dev before merging into staging.

For example J wanted to check efficiency of queries. We can run new pipelines in personal, then dev and include some rule of thumb for how long tasks within a pipeline should take. Checking time for pipelines to run could be part of checking dev is running as desired. (maybe its possible to build them in)

This is done by running the pipeline, clicking it once run in the pipelines/tasks section, looking at the chart and break down to see the time each part takes

It may be possible to automate some checks on time they take maybe as part of performance quality checks as J wants to know if once we hit staging if the behaviour changes so queries behave more expensively. Currenlty unsure best approach for this would require some exploration.
maybe queries log their time so we can see behaviour over time ... e.g. this query is getting more expensive (this seems a little out of scope currenlty)
- things to look at
  - spark for skew large shuffles spills to disk (think serverless handles this well though)
  - we could add comments on inception on how long we think any given process should take this is minimal effort early on when cognitive load is higher and useful later. e.g. "Expect 0-100 rows 1-3seconds could get large variation if lots of nulls in column X"
  we could record metrics worry about them later potentially```
  pipeline_metrics
- pipeline_name
- step_name
- duration_seconds
- row_count (optional)
- timestamp
  ```
PR check include
- some recording and comments on various dbx ui metrics for queries pipelines and tasks,

- reviewing all failed jobs and why in dev would be a good minimum before merge and tools including ai to analyse, use last merge potentially as the start of the period to look at.

- exploring system tables may be really useful 

# Staging

# Prod