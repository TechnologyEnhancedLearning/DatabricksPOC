# Not covered in POC


# Changes to make for the POC review qqqq
- get input on adhoc analysis template and file naming
- add adhoc read me to someone feedback objectives

# Not done qqqq
- add black to linting
- This document has excellent coverage and should be used to plan next steps and best practice examples [Dataquality](https://www.databricks.com/discover/pages/data-quality-management)
- read https://blogs.perficient.com/2025/03/19/delta-live-tables-and-great-expectations/
- environment branch rules stop pr directing against staging and prod make only correct branches mergeable (can always turn rule off in emergency)
- ~~version numbering~~ we can do release versioning manually makes more sense for us but it is not vital
- ~~enable copilot auto pr~~
- **IMP**seperated tests requiring rerunning pipelines from those that dont (data quality, sql sp)
  - different job per test type and different notebook


- ~~seperating dabs~~ dont see the advantage, team may have reason for why its desired
  - can do bronze, silver, gold etc
  - means modular deployment
  - cicd would need to detect changes in folders in order to know which dab to deploy
  - wheels again may be needed for code between dabs but maybe not
  - cluster dealing with smaller sizes
  - how to test

- requirements.txt and requirements-dev.txt need sorting, individual installs need removing




  [review existing policys](https://adb-295718430158257.17.azuredatabricks.net/compute/policies?o=295718430158257)


- config in the workspace level outside of git
  - this may be how we should manage the config
- J suggests https://www.databricks.com/discover/pages/access-control

# something here may help seperating unit integration etc tests
  [An example of some tests in NHS repo](https://github.com/nhsengland/NHSE_probabilistic_linkage/blob/main/tests/DAE_only_tests.py)
[An example of some tests in NHS repo2](https://github.com/nhsengland/NHSE_probabilistic_linkage/tree/main/tests)
- # MAGIC %run ../utils/dataset_ingestion_utils
- dbutils.notebook.run('../../notebooks_linking/clerical_review_evaluation', 0, {"params": params_serialized})