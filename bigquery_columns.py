import sys
import pandas as pd
import os
import time
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'you_credentials'

bigquery_client = bigquery.Client(project='your_project_name')

find_datasets_in_project = f'''
SELECT
 CONCAT("{sys.argv[1]}." ,schema_name, ".INFORMATION_SCHEMA.COLUMNS") as name
FROM
 `{sys.argv[1]}.INFORMATION_SCHEMA.SCHEMATA`
 '''

datasets_job = bigquery_client.query(find_datasets_in_project)
datasets_df = datasets_job.to_dataframe()

list_of_column = []

for row in datasets_job:
    column_query = bigquery_client.query(
    f'''
    SELECT
     table_catalog, table_schema,table_name , column_name
    FROM
     `{row[0]}`
     where column_name =  "{sys.argv[2]}"
    ''')

    if not column_query.to_dataframe().empty:
        list_of_column.append(column_query.result().to_dataframe())

df_of_occurances = pd.concat(list_of_column, ignore_index=True)
print(df_of_occurances.to_csv(sep='\t', index=False))
