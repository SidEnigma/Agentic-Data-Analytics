# Agentic Data Analytics

An autonomous AI-powered data analytics agent that ingests, processes, and visualizes data through natural language interaction — powered by [Opencode](https://opencode.ai).

## Agentic Workflow Using Opencode

This project uses **Opencode** — an AI-native CLI tool — as the agentic engine for end-to-end data analytics. The workflow is conversational: you describe what you want to analyze in natural language, and Opencode handles the rest.

### How the Workflow Works

1. **Ask in natural language** — Describe the analysis goal (e.g., "Analyze how programming language relates to reputation on Stack Overflow").
2. **Opencode explores the data** — It searches the project, discovers available tools (BigQuery, Python), and explores dataset schemas.
3. **Code is generated and executed** — SQL queries are written and run against BigQuery; Python scripts are created for analysis, quality checks, and visualization.
4. **Results are saved and organized** — Output files (CSV, TXT) and scripts are stored in `analysis/<topic>/` with a structured layout.
5. **Quality is verified** — Automated checks validate data integrity (nulls, ranges, consistency).
6. **Work is committed and reviewed** — A feature branch and pull request are created for human review.

### Tooling

| Tool | Purpose |
|------|---------|
| **Opencode** | AI agent orchestrating the entire workflow |
| **BigQuery (bq)** | Querying public datasets at scale |
| **google-cloud-bigquery** | Python client library for BigQuery |
| **Git/GitHub** | Version control and PR-based review |

## Analysis: Language Reputation on Stack Overflow

A case study in agentic data analytics — analyzing how programming language choice relates to Stack Overflow reputation (as a proxy for expertise/seniority).

### Key Findings

| Rank | Language | Developers | Avg Reputation | Median Reputation |
|------|----------|-----------|---------------|-------------------|
| 1 | Clojure | 4,468 | 12,228 | 3,031 |
| 2 | Scala | 21,670 | 10,101 | 1,968 |
| 3 | Haskell | 10,707 | 9,758 | 2,117 |
| 4 | Rust | 9,241 | 9,015 | 1,504 |
| 5 | Perl | 15,542 | 8,971 | 1,428 |
| 6 | Ruby | 45,574 | 8,905 | 1,894 |
| 7 | C++ | 118,173 | 8,480 | 1,351 |
| 8 | C# | 175,192 | 7,320 | 1,474 |
| 9 | Elixir | 2,583 | 7,270 | 2,190 |
| 10 | Go | 19,038 | 6,474 | 1,360 |
| 11 | Java | 246,121 | 6,265 | 1,097 |
| 12 | Lua | 5,940 | 6,098 | 913 |
| 13 | Dart | 12,558 | 5,761 | 703 |
| 14 | TypeScript | 51,082 | 5,739 | 1,145 |
| 15 | JavaScript | 338,217 | 5,709 | 1,069 |
| 16 | Python | 222,576 | 5,651 | 837 |
| 17 | PHP | 173,293 | 4,968 | 960 |
| 18 | Swift | 43,469 | 4,649 | 1,002 |
| 19 | MATLAB | 16,992 | 4,436 | 761 |
| 20 | Kotlin | 17,796 | 4,368 | 969 |
| 21 | R | 37,807 | 3,862 | 794 |
| 22 | SAS | 2,146 | 2,570 | 570 |

**Niche/specialist languages** (Clojure, Scala, Haskell, Rust) show the highest average reputation, likely because their smaller, more experienced communities correlate with deeper expertise.

**Mass-market languages** (JavaScript, Python, Java, PHP) have lower average reputations despite large developer bases — the larger talent pool includes more beginners and casual users.

### Methodology

- **Data source**: `bigquery-public-data.stackoverflow.posts_questions` joined with `bigquery-public-data.stackoverflow.users`
- **Filter**: Only users with reputation >= 100 (active contributors)
- **Reputation as proxy**: Stack Overflow reputation reflects peer recognition for quality contributions, used here as a proxy for expertise/seniority
- **Languages analyzed**: 22 major programming languages
- **SQL**: Tags column is pipe-separated and unnested; `APPROX_QUANTILES` used for median (approximate for performance on large data)
- **Saved table**: `project-504296d8-0479-471d-a5a.stackoverflow_analysis.language_reputation`

### Analysis Files

```
analysis/language_reputation_analysis/
├── sql/query.sql              — The BigQuery SQL query
├── python/analyze_reputation.py  — Python script to run the query via the client library
├── python/quality_check.py       — Quality validation script
├── results/results.csv           — Query results in CSV format
└── results/results.txt           — Query results in formatted table
```

## Getting Started

### Prerequisites

- Python 3.10+
- Google Cloud SDK with BigQuery access
- Required packages: `google-cloud-bigquery`

### Run the Analysis

```bash
# Install dependencies
pip install google-cloud-bigquery

# Authenticate with Google Cloud
gcloud auth login
gcloud auth application-default login

# Run the analysis query
cd analysis/language_reputation_analysis
python python/analyze_reputation.py

# Run quality checks
python python/quality_check.py
```
