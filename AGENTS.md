# AGENTS.md — For AI-Assisted Development

## Conventions

- **Language**: Python 3.10+
- **Code style**: Follow PEP 8
- **Testing**: Use pytest; tests go in `tests/`
- **Linting**: flake8 + mypy
- **Type hints**: Required for all function signatures

## Available Tools

- **gcloud & bq (BigQuery)** CLI are installed. The SDK bin dir has been added to the user PATH.
  - Verify: `gcloud --version`, `bq version`
  - Before using gcloud/bq in PowerShell, add the bin dir to PATH:
    ```powershell
    $env:Path += ";$env:LOCALAPPDATA\Google\Cloud SDK\google-cloud-sdk\bin"
    ```
  - **Project**: `project-504296d8-0479-471d-a5a` is configured via `gcloud config set project`.
  - **Query syntax** (PowerShell — use single quotes to avoid backtick issues):
    ```powershell
    bq query --use_legacy_sql=false --format=pretty 'SELECT COUNT(*) FROM `project.dataset.table`'
    ```
  - **Authenticated**: User has already run `gcloud init` and is logged in.

## Commands

- Run tests: `pytest`
- Lint: `flake8 src/`
- Type check: `mypy src/`

## Project Structure

```
src/            — Source code
tests/          — Test suite
data/           — Sample / input data
notebooks/      — Jupyter notebooks (exploration)
config/         — Configuration files
analysis/       — Analysis projects, each with:
    <topic>/
      sql/        — BigQuery SQL queries
      python/     — Python scripts (analysis, quality checks)
      results/    — Output data files (CSV, TXT, etc.)
      README.md   — Summary and key findings
```

## Agent Instructions

When making changes:
1. Read existing code to match conventions.
2. Add or update tests for new functionality.
3. Run `pytest`, `flake8`, and `mypy` before marking complete.
4. Keep README.md in sync with any new features or setup changes.
