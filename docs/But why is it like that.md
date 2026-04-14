# What is this doc

Every project has quirks, sometimes its for a reason. Drop them here if they don't fit any where else.

## Python library paths

It seems strange that we are not using empty __init__ and file pathing like
```
import sys

sys.path.append("/workspace/shared/Teamname")

from teamname_functions import core_func as core
```

> this nice clean approach won't work for us because github wont have the same path and won't work for username paths. Which is why the approach in the project is to determine the existing path, and then path to the needed libraries based on it. Using the approach above will work until used in github or deployed to usernamed paths. Putting libraries outside of username workspaces would mean the libraries can't be easily changed with the work depending on them because they are outside of source control. Another option would have been through the ui but has similar issues [adding local library dependencys microsoft learn dbx](https://learn.microsoft.com/en-gb/azure/databricks/compute/serverless/dependencies#create-common-utilities-to-share-across-your-workspace) 

## DUMMY_POLICY_FOR_BUNDLE_ID

Without having databricks.yml per target the bundle validate validates all yml included files at the top level, even if they are sync excluded e.g. prod excluding test files. So this policy should not show up in usage. It also mean we need to declare IDs for policys we are not using 
