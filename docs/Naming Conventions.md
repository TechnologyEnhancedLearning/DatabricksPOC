**AI Generated we can develop our own standard, but its a starting point**

# Databricks Asset Naming Conventions

This document defines naming standards for Databricks **pipelines, jobs, notebooks, and Python modules** to ensure consistency and maintainability.

---

## 1️⃣ Jobs

- **Bundle Key:** `snake_case` (used in YAML references)
  - Example: `medallion_refresh`, `integration_test_job`
- **UI Name:** `[<ENV>] Descriptive Name`
  - Include environment only if needed (`[dev] medallion_refresh`)
  - Example: `[staging] Integration Test Runner`
- **Guidelines:**
  - Use **descriptive verbs** for orchestrators: `refresh`, `run`, `trigger`
  - Avoid terms like `master`, `generic`, or `job1`
  - Keep names short (<40 characters) but meaningful

---

## 2️⃣ Pipelines

- **Bundle Key:** `snake_case`
  - Example: `pipeline_ods_ingestion`
- **UI Name:** `[<ENV>] Descriptive Name`
  - Example: `[dev] ODS Ingestion Pipeline`
- **Guidelines:**
  - Include domain and purpose in name
  - Prefix with `pipeline_` to distinguish from jobs

---

## 3️⃣ Notebooks

- **File Name:** `snake_case.ipynb`
  - Example: `run_tests.ipynb`, `load_ods_bronze.ipynb`
- **Notebook Title:** Optional markdown header inside the notebook for clarity
  - Example: `# ODS Bronze Loader`
- **Guidelines:**
  - Keep names descriptive and aligned with function
  - Avoid spaces and special characters

---

## 4️⃣ Python Modules / Packages

- **Package:** `snake_case`
- **Module:** `snake_case.py`
- **Classes:** `PascalCase`
- **Functions / Variables:** `snake_case`
- **Guidelines:**
  - Follow PEP8 conventions
  - Organize by domain or layer (e.g., `medallion`, `ods`, `reporting`)

---

## 5️⃣ General Recommendations

- Avoid embedding **implementation details** in names (e.g., `run_job1_pipeline2`)  
- Keep **consistent across environments**; use bundle variables for env-specific differences
- Maintain **separation of concerns**:
  - Jobs → orchestration
  - Pipelines → transformation
  - Notebooks → utilities/tests
  - Python modules → library code
- Document any deviations in this Markdown file for clarity
