# Language Reputation Analysis

Analysis of how programming language choice relates to Stack Overflow reputation (as a proxy for career success/expertise).

## Key Findings

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

## Methodology

- **Data source**: `bigquery-public-data.stackoverflow.posts_questions` joined with `bigquery-public-data.stackoverflow.users`
- **Filter**: Only users with reputation >= 100 (active contributors)
- **Reputation as proxy**: Stack Overflow reputation reflects peer recognition for quality contributions, used here as a proxy for expertise/seniority
- **Languages analyzed**: 22 major programming languages
- **SQL**: Tags column is pipe-separated and unnested; `APPROX_QUANTILES` used for median (approximate for performance on large data)
- **Saved table**: `project-504296d8-0479-471d-a5a.stackoverflow_analysis.language_reputation`

## Files

```
sql/query.sql              — The BigQuery SQL query
python/analyze_reputation.py  — Python script to run the query via the client library
python/quality_check.py       — Quality validation script
results/results.csv           — Query results in CSV format
results/results.txt           — Query results in formatted table
README.md                     — This file
```
