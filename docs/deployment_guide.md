# Deployment Guide

The current setup is a POC. We may decide to reduce the number of steps, but it is to support decision making.

DABs are deployed to 4 contexts.

**Personal** which is in your own user area folder e.g. users/first.lastname:nhs.net
This location has your branch folder in it and it has your bundle folder in it.

To deploy a DAB to your personal bundle folder:

Go to your personal folder
There will be an edit link to view as editable
To the right select the rocket
Select source for the bundle code to come from, this will be your repo
Target personal
Then click deploy

You should not deploy to the other targets from the ui. The other locations are shared so tests and git versioning should run first. Deploying to the other is done by merging to Dev, staging,prod git branches, which triggers Dab deployment processes using service principles.

**DEV**

After commiting and pushing follow the pull request link in databricks


