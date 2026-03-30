**AI Generated we can develop our own standard, but its a starting point**
# Databricks Naming Conventions

## Jobs
- **Internal ID (bundle key):** `snake_case` — e.g., `medallion_refresh`  
- **UI Name:** `[env] Descriptive Name` — e.g., `[staging] Refresh Medallion`  
- **Guidelines:**
  - Use **descriptive verbs**: `run`, `trigger`, `refresh`
  - Keep names short and meaningful
  - Avoid generic names like `job1` or `master`

## Pipelines
- **Internal ID:** `snake_case` — e.g., `pipeline_ods_ingestion`  
- **UI Name:** `[env] Descriptive Name` — e.g., `[dev] ODS Ingestion Pipeline`  
- **Guidelines:**
  - Prefix with `pipeline_` to distinguish from jobs
  - Include **domain and purpose** (`medallion`, `ods`, `reporting`)

## Notebooks
- **File Name:** `snake_case.ipynb` — e.g., `load_ods_bronze.ipynb`  
- **Optional Notebook Title:** `# ODS Bronze Loader`  
- **Guidelines:**
  - Keep names descriptive and aligned with function
  - Avoid spaces and special characters

## Python Modules / Packages
- **Module/File:** `snake_case.py`  
- **Classes:** `PascalCase`  
- **Functions / Variables:** `snake_case`  
- **Guidelines:**
  - Follow **PEP8 conventions**
  - Organize by **domain/layer** (`medallion`, `ods`, `reporting`)

## General Guidelines
- Names should describe **what the asset does**, not how it’s implemented
- Maintain **consistency across environments**
- Document any deviations in this file
- Encourage **clarity, reusability, and maintainability**
