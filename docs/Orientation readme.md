# Orientation Readme

## Whats in the project
- <foldername>-readme.md files for explaining what folders are for to keep them tidy it will help ai in future to
- notebooks folder for shareable source controlled exploratory notebooks (they do not get deployed to staging prod)
- scratch folder
  - the content is gitignored except the readme so this if for disposable code (also scratch- is gitignored so you can write scratch anywhere with scratch- as a file prepend)
- resources are for jobs and pipelines
- setup is for storing code that only runs once
- src is where all the code will live
- test is for tests
- databricks.yml controls how dabs are deployed
- pyproject.toml is for python configuration

## Good to know
- file structure where possible is reflected across src, resource, test so that it is easy to find what is relevant

## What to look at first
- an example that would (like the others) benefit from contribution
  - ingest
    - src/ingestion/ods_ingest.py
      - look at the folder structure of src
      - look at ods_ingest
    - look at the python file it references
      - src/utils/loaders.py
    - resources/pipeline/ingest/ods_ingestion.yml
      - look at resources top level and in pipeline (JB 04/03 reword)
      - notice how vars are passed
      - notice the anchor
  - dlt example (there are not any bronze stream tables so this isn't streaming sadly)
    - resources/pipeline/silver/isreporter_dlt.yml
    - src/silver/isreporter_dlt.py
    - src/utils/reporter_logic.py
- Test is a good place to look as well
  - tests/test-README.md

## Other things to look at
- service principles, pipelines, jobs
- .bundle folder in personal area
- .bundle in workspace
- https://github.com/TechnologyEnhancedLearning/DatabricksPOC
- https://github.com/TechnologyEnhancedLearning/DatabricksPOC/actions

