# Deployment Guide

The current setup is a POC. We may decide to reduce the number of steps, but it is to support decision making.

DABs are deployed to 4 contexts.

**Personal** - own workspace
which is in your own user area folder e.g. users/first.lastname:nhs.net
This location has your branch folder in it and it has your bundle folder in it.

To deploy a DAB to your personal bundle folder:

Go to your personal folder
There will be an edit link to view as editable
To the right select the rocket
Select source for the bundle code to come from, this will be your repo
Target personal
Then click deploy

You should not deploy to the other targets from the ui. The other locations are shared so tests and git versioning should run first. Deploying to the other is done by merging to Dev, staging,prod git branches, which triggers Dab deployment processes using service principles.

**DEV** - Shared data team space

After commiting and pushing follow the pull request link in databricks
"Successfully committed and pushed changes to branch "poc-dab-workflow"
Create a pull request on your git provider"

change the branch your merging into to Dev it defaults to base:main
read and check alll the pull request requirements (this poc doesnt have one set up but there will be a template in the "add a description" box)

once your happy create pull request

watch the automated tests to see if they fail if they do cancel the request and address the issue

there currently arnt branch rules stopping you merging however its good practice for this to be gated behind someone who didnt write the code. So ask someone who PRd to merge once the automatic tests have passed.

**staging** - shared pre deployment space with other teams

A lead dev should be in charge of deciding when enough work has gone into dev to move it to staging, typically you would move in quite quickly per change, but the dev environment allows to see what multiple changes do to Data teams shared space then they are merged together.

To make a pull request for staging got to git hub and create pull request and merging into staging.


**Prod**

the same processs as staging is repeated however prod will be lighter for easier deployment so will not run tests on the prod environment.

** Dev, Staging, Prod Merges**
These merges trigger tests in the databricks environments they can be viewed in databricks or in the actions tabs for the git repos.The tests can be triggered manually through notebooks as well.

See tests folder Run_Tests notebook this is what is triggered
