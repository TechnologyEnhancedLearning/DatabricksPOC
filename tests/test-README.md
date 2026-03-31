
# good to know
look in the top level toml file to see markers in use, add to them, they are good things to agree as a team i expect

# tests
- Tests live here
- Run_Tests allows manual running for devs
- Run_Tests has a job that triggers it for devops
- Run_Lint a nicety can manually target your file
- data-quality-tests check the data e.g. threshold for nulls
- test-reports currently lint report but future could have test thresholds and reports and gitpage in future
- integration-test for tests that interact with the environment or cant be issolated to a function
- units-tests refactor as much of our code to reuseable functions and unit tests them (should unit test everything but this would be a good start)
- Routes handled by conftest and toml
- @pytest.mark.integration_sql is important some tests like data-quality test may want to be marked as expensive, take a long time to run, staging-only, optional, or maybe even mergeable for ones we know sometimes the data will just be variable but we want to check before merging anyway, so we could run it in a different step if marked



# Spark config variables
We want spark to have bundle config values. They do for deployed dabs.
However on personal they dont unless you deploy running test.
We can code personal as defaults and fall back but this means they will be set both in databricks.yml
and the conftest.py so really we want to deploy or strip vars from databricks.yml
you can make a wrapper that uses personal values if there is not a dab deployment.
I dont want to duplicate configuration values. Can have a wrapper that provides hard code value if not set by databricks but unsure how would get personal area.



# How to write tests

Write functions that do one thing only if possible.
Inject in dependencys as arguments, like spark (so we can test against small static dfs not whole dbs )
File must start with test_ to be discoverably by pytest
Use test @pytest.mark markings where we may want exclusion or potential descriptions
Use classes to group tests
Use folders to group tests
Each test should test a single thing
AI writes them well so just check them and guide it to corner cases
A few unit tests, data-quality tests, and spark expect on pipelines is excellent coverage
Time taken writing tests is time ensuring code is reuseable next time and can be trusted when reused, they will also aid finding issues quickly
When querying data for exploration it is worth considering adding this into the shared notebooks, manual tests or automated testing :)

[An example of some tests in NHS repo](https://github.com/nhsengland/NHSE_probabilistic_linkage/blob/main/tests/DAE_only_tests.py)
[An example of some tests in NHS repo2](https://github.com/nhsengland/NHSE_probabilistic_linkage/tree/main/tests)

## Unit Tests
These are our best test, they run faster, cost less, they are for reuseable functions. If code can be refactored to be function based code it is a gift for the future as it makes it reuseable, and the tests make it reliable.

## Integration Tests
The tests cant be run in issolation, they may need IO, database access or may test two things interacting.
Or to see end to end behaviour e.g. a process that goes from bronze to silver to gold that you want to test end-to-end.

## E2E (end to end testing)
- full pipelines for example to **concider later currently out of scope**
- full pipeline
- run real thing not a test thing
- no mocking
- check end result not intemediatory steps
- need try and finally in case a fail causes clean up to be skipped

## UAT (User acceptance testing)
- **concider later automation currently out of scope**
- currently mixture of manual, colaborative, dev and analyst input
- recommend jira ticket review before behaviour testing.
- for buisness requirements
- buisness requirements

## data quality tests (needs seperating as requires pipelines to run and cost)
What do we expect of the data
What do we want to be warned about (we can always change thresholds later)
You can make manual tests for exploraion and use @python.mark.manual or some other mark we can use to exclude them
Pipelines will need rerunning so data is generated from the updated logic, there is a job/utis full_data_refresh job for this. If adding pipelines, this file will need adding to aswell so we can test on upto date data

## spark expect
Spark Expect occurs in pipeline code not the test folder. When writing checks into pipelines consider also writing data-quality tests for cicd.
dlt.expect is built in native so AI will help with it more easily than a package.


# Scratch manual test runner, and manual only run tests
Template can be trimmed and used without being sourced controlled for disposable tests. 
Manual only run, are not run by the test runner they are exploratory.



# Microsoft Learn Databrick Test Resources and Notes
[Microsoft Learn aligns strongly with our process](https://learn.microsoft.com/en-us/training/wwl-databricks/implement-development-lifecycle-processes-in-azure-databricks/4-implement-testing-strategy)
- our focus should just be unit first and alot of it
- when considering integration test we need to ensure we refactor everything to python and unit test it first, integration testing is not there to enable unit testing of sql, its for interaction
- for us user acceptance testing should first be built into jira ticket templates, with testers stating what they will look for, and B.A.s providing acceptance criteria. Then manual and automated testing can be concidered against these.

![Microsoft Learn aligns strongly with our process test triangle](https://learn.microsoft.com/en-us/training/wwl-databricks/implement-development-lifecycle-processes-in-azure-databricks/media/4-understand-test-pyramid.png)

[microsoft learn dbx git testing strategy](https://learn.microsoft.com/en-us/training/wwl-databricks/implement-development-lifecycle-processes-in-azure-databricks/4-implement-testing-strategy)
- this suggests test catalogues and schemas, the value of this is the catalogues dev, staging and personal schema should be data, not just test data. By using test catalogues and schemas its a closer comparison when does integration and e2e, (with a try catch finally to ensure per test suite data clean up). This approach is a step out of scope for now and the example in the PoC shows an integration test for csv using a temp volume area and clean up instead. As testing advance dev_test, staging_test, catalogues should be considered but the initially focus should be functional python unit tests.

# Other
- to improve the cicd test runner we could use subprocess, print errors under each cell but also store them and put them in the end step, this would allow us to print in github the specific failures. Not just the groups.

## Test Packages
### Great Expectations
We can use packages like great expectation (like fluent assertions) for two things
- nice dot notation
- within our data-quality tests give us some short hand
- built into pipelines to fail them early ... think could run specific pytest too if we like
- some stackoverflow is negative despite actual GE staff trying to contextualise it
- other nhs teams have similarly mixed feelings

### PyTest
- is a common test runner package which is why it is used here, there may be more suited ones
  - notebook based testing did not seem as good
  - there are others test packages but none stood out
  - pytest will have lots of documentation and stackoverflow, as it is mature and common

# Trouble shooting
- please add to this section

# useful ref (not used for setup but good)
[NHS docs on unit tests, what to test, names etc ](https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/unit-testing/)
- provides good guidance




[dbx docs basic unit tests ok](https://docs.databricks.com/aws/en/notebooks/testing?language=SQL)

[dbx blog testing](https://community.databricks.com/t5/technical-blog/writing-unit-tests-for-pyspark-in-databricks-approaches-and-best/ba-p/122398)
- agrees with this poc approach good explanation
- "Control Notebook Execution: Wrap main execution logic in if __name__ == "__main__" blocks to prevent it from running during imports." <- not in poc atm

[notebooks as test runner](Databricks - How to create your Data Quality Checks Notebooks)
this is a really nice approach and i like it because it is interactive, and it turns a notebook into a runner and is threaded. I havent used it because i want test_ .py files that trigger via pytest for automation. however i like this for data-quality because data quality is often, "alert this looks off" and so then the response is to explore it. by automating it means checks always happen and we aways seem them because the git action will give us a fail and then we need to rewrite the code (or hit merge anyway if it is some specific data thing maybe but this would be a risky habit as tests will start being ignored). But notebooks are more exploritary.

[Great expectations didnt find very useful](https://blogs.perficient.com/2025/03/19/delta-live-tables-and-great-expectations/)