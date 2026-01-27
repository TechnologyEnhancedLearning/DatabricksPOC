# tests
- Tests live here
- Run_Tests allows manual running for devs
- Run_Tests has a job that triggers it for devops
- Run_Lint a nicety can manually target your file
- data-quality-tests check the data e.g. threshold for nulls
- test-reports currently lint report but future could have test thresholds and reports and gitpage in future
- integration-test for test that interact with the environment or cant be issolated to a function
- units-tests refactor as much of our code to reuseable functions and unit tests them (should unit test everything but this would be a good start)
- Routes handled by conftest and toml

# useful ref (not used for setup but good)

[dbx docs basic unit tests](https://docs.databricks.com/aws/en/notebooks/testing?language=SQL)

[dbx blog testing](https://community.databricks.com/t5/technical-blog/writing-unit-tests-for-pyspark-in-databricks-approaches-and-best/ba-p/122398)
- agrees with this poc approach good explanation
- "Control Notebook Execution: Wrap main execution logic in if __name__ == "__main__" blocks to prevent it from running during imports." <- not in poc atm

