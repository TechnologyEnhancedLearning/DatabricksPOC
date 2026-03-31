# Deployment Guide

*Refer to databricks.yml*

The current setup is a POC. We may decide to reduce the number of steps, its purpose is to support decision making by offering comprehensive options.

DABs are deployed to 4 contexts.

**Personal** (own workspace)

Found in your own user area folder e.g. users/first.lastname:nhs.net
This location has your branch folder in it, and your .bundle folder in it.

To deploy a DAB to your personal bundle folder:

1. Go to your personal folder.
2. There will be an edit link to view as editable.
3. To the right select the rocket.
4. Select source for the bundle code to come from, this will be your repo
5. Target personal
6. Then click deploy

You should not deploy to the other targets from the UI. The other locations are shared so code is deployed by cicd with tests and peer review. Deployment is done by merging to Dev, staging, prod git branches, which triggers Dab deployment processes using service principles.

**DEV** - Shared data team space

After commiting and pushing in the databricks UI then follow the pull request link in databricks. The link in DBX UI is :
"Successfully committed and pushed changes to branch 'poc-dab-workflow' Create a pull request on your git provider".

Your taken to github.com pull-request UI. **Important:** Change the branch your merging into to Dev (it defaults to base:main)
read and check all the pull request requirements.

Once your happy create pull request or draft.

Watch the automated github pull request checks. See if they fail if they do cancel the request and address the issue.

Once the checks have passed ask someone to peer review. Then once approved merge.
Check Merge pipeline in github succeeds.
Then check in the databricks environment.

**Staging** - shared pre deployment space with other teams

A lead dev should be in charge of deciding when enough work has gone into dev to move it to staging, typically you would move in quite quickly per change, but the dev environment allows to see what multiple changes do to Data teams shared space then they are merged together.

To make a pull request for staging got to git hub and create pull request and merging into staging.


**Prod**

The same processs as staging is repeated however prod will be lighter for easier deployment so will not run tests on the prod environment.

** Dev, Staging, Prod Merges**
These merges trigger tests in the databricks environments they can be viewed in databricks or in the actions tabs for the git repos.The tests can be triggered manually through notebooks as well.

See tests folder Run_Tests notebook this is what is triggered
