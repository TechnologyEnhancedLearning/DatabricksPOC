# Changes to make for the POC review
- get input on adhoc analysis template and file naming
- add adhoc read me to someone feedback objectives

# Not covered in POC
- **try moving vars to const files etc and out of bundle**
include:
    - 'variables/*.yml' if execute in order might be able to put vars in folders based off headings, may affect running in personal area before deploy?

# Not done
- explore what black does in toml
- This document has excellent coverage and should be used to plan next steps and best practice examples [Dataquality](https://www.databricks.com/discover/pages/data-quality-management)
- read https://blogs.perficient.com/2025/03/19/delta-live-tables-and-great-expectations/
- need public repo for branch rules, theyre not tweaked so cant just be exported but
	- can set deployment rules
	- and rules per branch .yml file
- github auto merge staging
- **version numbering**
- enable copilot auto pr
	- recommend enable in branch rules
	- and require one reviewer
	- /addinstructions as a command in databricks ai can work so can put user space or work space instructions
- lakehouse monitoring!
- seperated tests requiring rerunning pipelines from those that dont (data quality, sql sp)
- different job per test type and different notebook


- seperating dabs
  - can do bronze, silver, gold etc
  - means modular deployment
  - cicd would need to detect changes in folders in order to know which dab to deploy
  - wheels again may be needed for code between dabs but maybe not
  - cluster dealing with smaller sizes
  - how to test

- are requirements txt still needed is it due to python version and setup in git pipeline that i am not just using toml?


