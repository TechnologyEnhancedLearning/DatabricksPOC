- are requirments txt still needed is it due to python version and setup in git pipeline that i am not just using toml?
- i have 2 dlt pipeline version check which is right its in silver resources
- check deploys
- designated test cluster or one per env
- bundle test runners running old code!
  - unsure if something to do with sync options
  - remember develop work a bit different
  - seems wrong it wouldnt be a fresh copy
  - seems wrong deploy wouldnt also build a bundle rather tan deploying something old


  # 🔍 DAB Deployment Troubleshooting Checklist - generated for notebook test runner triggered by git not using latest notebooks, could be due to develop deploy, or resource sync not including test, or something else??? 

### 1. Check for Resource Prefixing (Development Mode)
If `mode: development` is active, resources are renamed to avoid conflicts.
* **The Look:** Search for `[dev <your-user-id>]` in the Databricks UI.
* **The Fix:** Switch to `mode: production` in your [databricks.yml](https://docs.databricks.com) or explicitly set a `name_prefix`.

### 2. Verify Inclusion Logic
If your resource YAMLs aren't in the main file, they must be explicitly imported.
* **The Fix:** Ensure your `databricks.yml` includes the path:
```yaml
include:
  - resources/*.yml
