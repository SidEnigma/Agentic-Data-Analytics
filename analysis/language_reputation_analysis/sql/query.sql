SELECT
  tag AS language,
  COUNT(DISTINCT q.owner_user_id) AS developer_count,
  CAST(ROUND(AVG(u.reputation)) AS INT64) AS avg_reputation,
  APPROX_QUANTILES(u.reputation, 100)[OFFSET(50)] AS median_reputation,
  MAX(u.reputation) AS max_reputation
FROM (
  SELECT id, owner_user_id, tag
  FROM `bigquery-public-data.stackoverflow.posts_questions`,
  UNNEST(SPLIT(tags, '|')) AS tag
) q
JOIN `bigquery-public-data.stackoverflow.users` u
  ON q.owner_user_id = u.id
WHERE LOWER(tag) IN (
    'python', 'javascript', 'java', 'c#', 'c++', 'php', 'ruby', 'go',
    'rust', 'swift', 'kotlin', 'typescript', 'scala', 'r', 'perl',
    'haskell', 'lua', 'dart', 'elixir', 'clojure', 'sas', 'matlab'
  )
  AND u.reputation >= 100
GROUP BY language
ORDER BY avg_reputation DESC
