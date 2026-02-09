# Context

Standardising naming for commits can be useful for autogenerating versioning changelogs.
- for example this git repo is for a tool that does this, on the right hand side you can see for their package they have release versions and clicking on them you can see a changelog
[semver example using their git repo for their package](https://github.com/semantic-release/semantic-release)
This repo explains the commit naming, and demonstrates it. Here is the list of changes theyve made as a generated changelog [semver package releases changelog](https://github.com/semantic-release/semantic-release/releases)

It can be useful when PRing for humans and AI Prs too. 
We may want to define out own standardisation.

## Commit names
fix(pencil): stop graphite breaking when too much pressure applied

### E.g.

#### FEAT — new capability / behaviour
feat(lms): add derived completion_status for statutory training
feat(pipeline): publish daily LMS compliance snapshot to curated layer
feat(model): expose expiry_date logic for mandatory training

#### FIX — bug / incorrect logic
fix(sql): correct join logic causing duplicate learner records
fix(model): handle null end dates for honorary contracts
fix(lms): resolve incorrect compliance flag for bank staff

#### REFACTOR — same behaviour, better structure
refactor(pipeline): move learner completion logic from SQL to PySpark
refactor(pipeline): replace usp_UpdateLMSCompliance with Databricks job
refactor(model): extract completion calculation into reusable function
refactor(pipeline): decouple LMS rules from ingestion logic

#### TEST — tests only
test(model): add unit tests for completion status calculation
test(pipeline): replace LMS integration test with isolated unit tests
test(lms): cover edge cases for training expiry logic

#### PERF — performance improvements
perf(pipeline): reduce LMS compliance job runtime by optimising joins
perf(sql): remove redundant subqueries from compliance extract

#### CHORE — housekeeping, no behaviour change
chore(notebook): clean up LMS compliance analysis notebook
chore(ci): update Databricks job parameters for LMS pipelines

#### SCHEMA — data shape changes
schema(lms): add staff_group_code to training_completion table
schema(lms)!: rename staff_id to person_id across LMS marts

#### DOCS — documentation only
docs(lms): document compliance logic and ESR alignment assumptions

#### BUILD / CI — tooling & pipelines
ci(lms): run unit tests for PySpark models on pull requests
build(pipeline): parameterise LMS job for multiple environments


## Branch naming

Make branches from main.

TODO: See learning hub branch names and documentation
Something like

feature/<issue-number>-<short-description>
fix/<issue-number>-<short-description>
refactor/<issue-number>-<short-description>
hotfix/<issue-number>-<short-description>

**Branch Naming Examples**

**Feature branches** - New functionality or enhancements:
feature/101-add-learner-dashboard
feature/102-enable-course-progress-tracking
feature/103-integrate-esr-user-data
feature/104-add-training-completion-export

**Fix / bug branches** - Bug fixes or corrections:
fix/201-correct-login-session-timeout
fix/202-resolve-duplicate-learner-rows
fix/203-handle-null-expiry-dates

**Refactor branches** - Refactoring code without changing behaviour:
refactor/301-extract-user-service
refactor/302-move-completion-calculation-to-pyspark
refactor/303-cleanup-lms-notebook

**Hotfix / urgent branches** - Critical issues requiring immediate production deployment:
hotfix/401-critical-login-error
hotfix/402-fix-mandatory-training-bug

**Experiment / spike branches** - Temporary or exploratory work:
spike/501-pyspark-performance-test
spike/502-new-dashboard-ui-prototype

