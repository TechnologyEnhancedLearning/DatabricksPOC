
# Python
*Python is strongly recommended in DBX and microsoft docs for use in databricks*
- reuseable
- testable
- Whereas SQL gets unreadable and hard to pr quickly with nested queries and window functions
- advantages of package ecosystem
- Python handles complex calculations, conditional logic, string manipulations, and date arithmetic more cleanly than SQL.

## Making python easy

- AI to translate (specific context has been provided in assistant AI context files)
- do most repeatable logic first
- do easiest tasks in python use it for increasingly complex tasks over time
- see other nhs dbx projects on databricks and github (see refs below and [list of RAP projects](https://github.com/NHSDigital/data-analytics-services?tab=readme-ov-file#rap-publication-repositories))
- use pull request ai
- ask other dbx teams for review and knowledge share
- co-code it with someone else
- use unit tested existing python code as a reference


## SQL
- still ideal for reads on gold
- for one off queries which wont be reused in any way (queries may have parts to them that could in fact be useful python functions)


# Refs
[pyspark RAP](https://nhsdigital.github.io/rap-community-of-practice/training_resources/pyspark/) put this in PR
- pyspark dynamic modular queries lazy.

[python style guide, can be useful not just to lint but to help name etc](https://peps.python.org/pep-0008/)

[python functions nhs guide](https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/python-functions/)
[python unit test nhs guide](https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/unit-testing-field-definitions/)
[python unit test nhs guide 2](https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/unit-testing/)
[NHS python pyspark style guide](https://nhsdigital.github.io/rap-community-of-practice/training_resources/pyspark/pyspark-style-guide/)
"We avoid using pandas or koalas because it adds another layer of learning. The PySpark method chaining syntax is easy to learn, easy to read, and will be familiar for anyone who has used SQL."
[another pyguide useful but less so](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
[pyspark RAP useful but less so](https://nhsdigital.github.io/rap-community-of-practice/training_resources/pyspark/)
