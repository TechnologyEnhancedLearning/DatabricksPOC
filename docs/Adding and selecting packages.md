# Adding Packages

## Warning
- AI tends to suggest packages unnecesarily, and list them as imports


## Checks before adding packages
- Is the package already in use within the project?
- Is a similar package already in use, can we use only one of the two? (unit tests should allow confidence in changing pre-existing package)
    - search (to see where used)
    - requirements.txt and requirements-dev.txt
- Is the package still:
    - regularly updated 
    - trusted 
    - managed by a team not an individual
    - has lots of downloads?
    - As a reference for how to check
        - E.g. releases [pandas history](https://pypi.org/project/pandas/#history)
        - E.g. versioning and downloads [pepy version history](https://pepy.tech/projects/pandas?timeRange=threeMonths&category=version&includeCIDownloads=true&granularity=daily&viewType=line&versions=3.0.1%2C3.0.0%2C3.0.0rc2)
- Is it necessary?
    - niceties like packages providing nicer syntaxes can make AI less-effective and increase knowledge requirement for engaging with ecosystem. So pros and cons should be weighed (potential including the team)
    - they increase the maintenance surface
- Is there a better package?
    - More downloaded/maintained
    - Related to existing package
    - Recommended for databricks
    - Is more future proof


## How to add packages

- Add to AI prompts global and individual instructions to know we are using the package so it can make recommendation of when to apply it
- Add to toml (if needs some configuration)
- Add to requirements.txt and requirements-dev.txt so they are global not local, and usable in git pipeline
    - requirements.txt should be the same as requirements-dev.txt except for packages not used in prod such as test and lint
    - requirements-dev.txt is for all environments excepts prod
    - pin version numbers when adding packages to these files
    - include a comment on why it was added
- If running manually in a code file you will need to add to the top cell
```
# Check if this is a manual interactive session (User UI)
ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
is_manual_user = ctx.jobId().isEmpty() 

# DABs Jobs Pipelines CICD environments, Github provide the packages but manual development requires it to be applied (see discussion in Add packages docs)
if is_manual_user:
    print("User UI detected. Syncing dev packages...")
    %pip install -r ../requirements-dev.txt
    dbutils.library.restartPython()
else:
    print("Automated Job/Pipeline detected. Skipping dev install.")
```

# Challenges with managing packages
*A better approach would be desireable for how we manage packages*
- we want to
    - standardise versions of packages
    - ideally only install them once
    - not reinstall if cluster has the packages
    - not need to manually set them up on the cluster
    - have them source controlled
    - not need to define them per notebook causing duplication and mixed version
    - not define them anywhere except requirements-dev.txt and requirement.txt because we dont want multiple sources of truth
    - not require analysts to have to command line install all the time
- pipelines/jobs need to reference installing requirement.txt or requirement-dev.txt
- dabs deploy requirments-dev.txt
- github useses requirements-dev.txt for its tests
- cluster enviroments can be set to point at the however
    - if done to a branch requirements their target will need updating per branch change
    - if targetted outside a branch the packages are outside of source control so updating requirments-dev.txt wont instantly change behaviour so issues may be missed
- Other solutions other teams may be using
    - externally controlled (maybe acceptable if rarily changed), part of a seperate repo with utilities which provides a whl
    - a _bootstrap environment file that Ive seen in some projects that can be called





# Extras
- we are not currently creating package wheels with own libraries to apply to clusters 18/3/26
- [JAR may be relevant for wheel](https://learn.microsoft.com/en-gb/azure/databricks/release-notes/release-types)
- [sharing our packages across dbx ... may not be useful as may not help with git](https://learn.microsoft.com/en-gb/azure/databricks/compute/serverless/dependencies#create-common-utilities-to-share-across-your-workspace)
