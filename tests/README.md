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
- @pytest.mark.integration_sql is important some tests like data-quality test may want to be marked as expensive, take a long time to run, staging-only, optional, or maybe even mergeable for ones we know sometimes the data will just be variable but we want to check before merging anyway, so we could run it in a different step if marked

# List of pytest.mark and what they are for should go here
:)

# Spark config variables
We want spark to have bundle config values. They do for deployed dabs.
However on personal they dont unless you deploy running test.
We can code personal as defaults and fall back but this means they will be set both in databricks.yml
and the conftest.py so really we want to deploy or strip vars from databricks.yml
you can make a wrapper that uses personal values if there is not a dab deployment.
I dont want to duplicate configuration values. Can have a wrapper that provides hard code value if not set by databricks but unsure how would get personal area.

# useful ref (not used for setup but good)

[dbx docs basic unit tests ok](https://docs.databricks.com/aws/en/notebooks/testing?language=SQL)

[dbx blog testing](https://community.databricks.com/t5/technical-blog/writing-unit-tests-for-pyspark-in-databricks-approaches-and-best/ba-p/122398)
- agrees with this poc approach good explanation
- "Control Notebook Execution: Wrap main execution logic in if __name__ == "__main__" blocks to prevent it from running during imports." <- not in poc atm

[notebooks as test runner](Databricks - How to create your Data Quality Checks Notebooks)
this is a really nice approach and i like it because it is interactive, and it turns a notebook into a runner and is threaded. I havent used it because i want test_ .py files that trigger via pytest for automation. however i like this for data-quality because data quality is often, "alert this looks off" and so then the response is to explore it. by automating it means checks always happen and we aways seem them because the git action will give us a fail and then we need to rewrite the code (or hit merge anyway if it is some specific data thing maybe but this would be a risky habit as tests will start being ignored). But notebooks are more exploritary.