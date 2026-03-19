# What is this doc

Every project has quirks, sometimes its for a reason. Drop them here if they doesnt fit any where else.

## Python library paths

It seems strange that we are not using empty __init__ and file pathing like
```
import sys

sys.path.append("/workspace/shared/Teamname")

from teamname_functions import core_func as core
```
> this nice clean approach wont work for us because github wont have the same path and wont work for username paths. Which is why the approach in the project is to determine the existing path, and then path to the needed libraries based on it. Using the approach above will work until used in github or deployed to usernamed paths. Putting it outside of username workspaces would mean the libraries can't be easily changed with the work depending on them. Another option would have been through the ui but has similar issues [adding local library dependencys microsoft learn dbx](https://learn.microsoft.com/en-gb/azure/databricks/compute/serverless/dependencies#create-common-utilities-to-share-across-your-workspace) 

