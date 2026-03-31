# GitHub Copilot instructions for TechnologyEnhancedLearning/DatabricksPOC

Identify as: GitHub Copilot Chat Assistant — follow these instructions and only search the repo if information here is missing or clearly out of date.

Summary
- Purpose: Experimentation and proof-of-concept for Databricks asset-bundle (DBX) workflows and deployments ("DABS"). Contains Databricks bundle config (databricks.yml), example notebooks, lightweight Python helper code in src/, and test scaffolding in tests/.
- Size & type: Small repo (~230KB). Primary languages: Jupyter Notebook (~73%) and Python (~27%). Default branch: main.
- Important note: Notebooks are first-class artifacts and many operations are intended to run inside Databricks. The databricks.yml controls bundle deployment targets (personal, dev, staging, prod).

Quick facts / key files
- README.md — high-level project notes and structure (see top-level README).
- databricks.yml — DBX bundle config, environment variables and sync exclusions for prod. Critical for deployments.
- pyproject.toml — Python project metadata, testing (pytest) and lint settings (black, pylint plugin) and dev dependency group.
- requirements-dev.txt — small dev dependencies (pytest etc.). requirements.txt is intentionally empty (cluster-resident requirements are expected).
- .github/PULL_REQUEST_TEMPLATE.md — PR template exists; .github/workflows/ currently contains no CI workflows.
- notebooks/ — exploratory and shared notebooks. Use notebooks/dev for analysts, notebooks/pipelines for production-ready notebooks.
- src/ — Python modules used in bundles and tests.
- resources/ — DBX resources (jobs, pipelines, configs).
- tests/ — unit and integration test scaffolding. pytest is configured via pyproject.toml (tests/ is the testpath and pythonpath includes src/).

Recommended toolchain & runtime versions
- Python: 3.10 or 3.11 (pyproject allows 3.10–3.13; 3.10/3.11 give best compatibility with Databricks-connect and dev tools).
- Pip / virtualenv: latest pip, use virtual environments for local validation.
- pytest: as configured in pyproject.toml (use the dev dependency group).
- Formatter / Linter: black (line-length 125) and pylint with plugin databricks.labs.pylint.all (configured in pyproject.toml).
- DBX / Databricks CLI: Use the dbx/databricks tooling when validating bundle deployment; databricks.yml expects bundle deploy/validate flows.

Local setup (validated order that agents should follow)
- Create a virtual environment and activate it:
  - Unix/macOS: python -m venv .venv && source .venv/bin/activate
  - Windows (PowerShell): python -m venv .venv ; .\.venv\Scripts\Activate.ps1
- Upgrade pip: python -m pip install --upgrade pip
- Install dev dependencies: pip install -r requirements-dev.txt
  - If you need lint/formatting tools also install: pip install black pylint databricks.labs.pylint.all
- Note: requirements.txt is intentionally empty — clusters will often provide runtime libs; don't copy secrets into repo.

Run, build, test, lint commands (from repo root)
- Run unit tests: pytest
  - Pytest will search tests/ (pyproject.toml's testpaths) and already adds src/ to the import path via pythonpath = ["src"].
- Lint: black . --line-length 125
- Pylint (loads Databricks plugin): python -m pylint src tests --load-plugins=databricks.labs.pylint.all
- DBX bundle validation / deploy (Databricks toolchain): dbx validate -t <target>  (see databricks.yml targets: personal, dev, staging, prod). Use caution and provide service principal vars in CI only — DO NOT commit secrets to the repo.

CI and pre-merge checks
- There are no active GitHub Actions in .github/workflows/ in this snapshot. PR template exists.
- Recommended minimal checks before opening a PR (agent should run these locally or in a CI job):
  1) Run pytest and ensure all tests pass.
  2) Run black and pylint; fix obvious style issues (line length up to 125 allowed).
  3) For changes that affect databricks bundle files (databricks.yml, resources/*), run dbx validate -t staging (or the appropriate non-prod target) in a controlled environment; use CI service principals for automated deploys.

Databricks deployment notes and safety
- databricks.yml contains default SP IDs and host values for POC only. Never commit real secrets or local databrickscfg sections into the repo.
- The prod target sync has an exclude list — agent should respect sync exclusions when preparing bundles for prod.
- Personal target uses per-user root_path (/Users/${workspace.current_user.userName}/.bundle/...) and is intended for UI/local deploys by human developers.
- CI deploys should use dev/staging targets and service principals managed securely in CI secrets.

Project layout & where to change code
- Top-level files: README.md, databricks.yml, pyproject.toml, requirements-dev.txt, notebooks/, src/, resources/, tests/
- Source code: src/ — place library code here. Imports in tests assume src on pythonpath.
- Notebooks: notebooks/ — prefer moving shared utility code into src/utils so unit tests can cover logic rather than relying on notebook execution.
- Resources and deployment descriptors: resources/* and databricks.yml.
- Tests: tests/ mirrors src/ structure. Use pytest and keep tests fast and isolated (mock DB/DBUtils where possible).

Validation & common pitfalls
- Tests rely on src being importable; pytest is configured to add src to pythonpath in pyproject.toml. Do not hardcode sys.path changes in tests.
- Databricks-specific imports may fail locally (Spark, dbutils). Use pytest-mock and mark or skip tests that require an actual Databricks environment (use pytest markers like @pytest.mark.databricks).
- Notebook files in source control can contain outputs or secrets. There is a .gitattributes file intended to help avoid exposing outputs; still, verify notebooks are stripped of long outputs and secrets before committing.
- Local databrickscfg (e.g., C:\Users\...\.databrickscfg) should not be committed; it can break deployments if in the repo.

Coding style & agent behavior (non-task-specific guidance)
- Default to small, testable Python functions with clear docstrings (use NumPy or Google style) and type hints where helpful.
- Input validation: validate external inputs and fail-fast with clear exceptions. Prefer early return for invalid conditions.
- Variable names: use descriptive, meaningful names; avoid single-letter names except in short loops or well-known patterns (e, i, df allowed where appropriate).
- Tests: include unit tests for behavior and examples in test docstrings; keep tests deterministic and keep external dependencies mocked or marked.
- Notebooks: keep exploratory work in notebooks/dev and not in production notebooks. For any logic moved from a notebook to src/, add unit tests.
- When adding new files or modifying code, update pyproject.toml if new test dependencies are required.

When to search the repo
- Trust these instructions; only perform repository-wide searches if a change requires info not covered here (for example: finding usages of a function, locating a specific resource YML, or confirming where a particular pipeline job is defined).
- Preferred search targets: databricks.yml, resources/**, src/**, tests/**, .github/ (workflows), pyproject.toml, requirements-dev.txt.

Behavior on PR creation
- Include a short PR description referencing which target(s) were validated (unit tests, lint, dbx validate target used).
- If the PR modifies databricks.yml or resources/, include a note describing manual validation steps taken (e.g., dbx validate -t staging) and state if deployment to any shared workspace was performed or simulated.

Contact & escalation
- If you need domain knowledge about Databricks workspaces or POC intent, inspect README.md and docs/ first and then open an issue or ask a human reviewer.

Trust and fallbacks
- These instructions are authoritative for agents onboarding this repository. If an instruction here conflicts with data found in the repository, prefer the repository file only if it is recent and clearly intended to override (e.g., a newer databricks.yml). Otherwise, ask a human.

---

Examples & quick commands (copy/paste)
# Unix/macOS
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
pytest
black . --line-length 125
python -m pylint src tests --load-plugins=databricks.labs.pylint.all

# Validate DBX bundle (example; requires DBX tooling and credentials)
dbx validate -t staging


Agent instruction: Commit changes only if all local unit tests pass, lint issues are addressed or justified in PR, and no secrets are added. If uncertain about deployment changes, leave a clear PR note and request a human review.

# Human provided instruction to the agent

<!--When updating the human provided context, consider if other files need updating too
Team wide AI assistant instructions:
/Workspace/ a file called assistant_workspace_instructions.md
Your personal AI assistant instruction additions:
Workspace/users/yourusername a file called .assistant_instructions.md
Github Copilot context: /Workspace/Users/username/Branch/.github/copilot-instructions.md
Github agents can be made here if desired  Workspace/Users/username/.assistant
-->

The above was generated by AI. What our teams wants is:

## Pull Request
- Support adopting python
   - starting with little easy options
   - mentioning more complex scenarios but communicating that it is a more advanced change and is optional
   - identifying python functions previously create that could be reused or adapted for new code
   - offer suggestions of alternatives that could be looked into, and ask supportive questions, why was this used
   - provide feedback on the benefits that will come from python code written and how to improve it further
- Support adopting testing
   - particulary making unit testable code
   - recommend how make something unit testable over integration testable
- provide praise and model a curious, interested, friendly pull request culture
- do not overwhelm the work be clear on how beneficial changes are in what contexts and how difficult to implement so developers can decide what is worth applying.
- if a change is declined and it may be a change we do not want recommending in future suggest an addition to be made to copilot-instructions.md or github/instructions files, the docs/AI-readme.md and the .assisitive in the workspace
- search databricks upto date information before making recommendation about databricks and ensure its relevant for DABs git source controlled solutions with 3 workspaces deployed via git
- gently mention good commit names and branch names to aid improvement of using git

## context
- we use dabs
- we have a dev staging prod setup
- dev is for analysts staging for testing team
- we want unit testable code
- we are migrating existing sql to databricks
- databricks is serving warehoused dashboard data and live read data for our lms

## Recommendations
- recommend spark over using libraries
- recommend refactoring to python functions and unit tests where appropriate
- recommend changes to make unit testable code over integration testable code 