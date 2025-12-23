# To use this folder
- need proper pathing
- need toml and test config set up

# Integration Tests

These tests are not purely functional they interact with the databricks environment.
They will need dbutils spark and the file system.
We should write code to keep these concerns seperate where we can to enable clean testing

Integration tests will be triggered by git action or can be triggered via a notebook.
They will run in databricks environment where as unit tests will be purely functional so can be run
via a notebook in databrick or as a gitaction within github.

# Notes to help future implementation

## A databricks job to be triggered on deploying a dab i expect
Just pseudo code
```
bundle:
  name: my-feature-tests

resources:
  jobs:
    test_job:
      name: "PyTest Runner"
      tasks:
        - task_key: run_pytest
          new_cluster:
            spark_version: "13.3.x-scala2.12"
            node_type_id: "Standard_DS3_v2"
            num_workers: 1
          notebook_task:
            notebook_path: ./somepath/run_integration_tests.py

```
Something to add to the run tests py
```
# Very important: Exit with the code from pytest 
# so the GitHub Action knows if it failed or passed
if retcode != 0:
    sys.exit(retcode)
```