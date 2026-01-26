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
