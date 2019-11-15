# bigquery_column_finder
Helper to find which tables have a given column

Currently there is no way to find where certain columns are used within BigQuery tables without query each dataset individually

## Use

1. Add the path to your GCS/BigQuery credentials
2. Add your project_id to the `bigquery_client`
3. run with `python bigquery_columns.py project_id_to_search column_name_to_search_for`
