# Adding Packages

## Warning
- AI tends to suggest packages unneccesarily, and list them as imports


## Checks before adding packages
- Is the package already in use within the project?
- Is a similiar package already in use, can we use only one of the two? (unit tests should allow confidence in changing prexisiting package)
    - search (to see where used)
    - requirements.txt and requirements-dev.txt
- Is the package still regularly updated, trusted, managed by a team not an individual and lots of downloads?
    - E.g. releases https://pypi.org/project/pandas/#history
    - E.g. versioning and downloads https://pepy.tech/projects/pandas?timeRange=threeMonths&category=version&includeCIDownloads=true&granularity=daily&viewType=line&versions=3.0.1%2C3.0.0%2C3.0.0rc2
- Is it necessary?
    - niceties like packages providing nicer syntaxes can make AI effective less and increase knowledge requirement for engaging with ecosystem so pros and cons should be weighed potential including the team
    - they increase the maintenance surface
- Is there a better package?
    - More downloaded/maintained
    - Related to existing package
    - Recommended for databricks
    - Is more future proof


## How to add packages

- Add to AI prompts global and individual instructions to know we are using the package so it can recommend its usage
- Add to toml (if needs some configuration)
- Add to requirements.txt and requirements-dev.txt so they are global not local, and usable in git pipeline
    - requirements.txt should be the same as requirments-dev.txt excluding packages not used in prod such as test and lint
    - requirements-dev.txt is for all environments excepts prod
    - pin version numbers when adding packages to these files
    - include a comment on why it was added


# Extras
- we are not currently creating package wheels with own libraries to apply to clusters 18/3/26
- [JAR may be relevant for wheel](https://learn.microsoft.com/en-gb/azure/databricks/release-notes/release-types)
- [sharing our packages across dbx ... may not be useful as may not help with git](https://learn.microsoft.com/en-gb/azure/databricks/compute/serverless/dependencies#create-common-utilities-to-share-across-your-workspace)
