import pyodbc
import pandas as pd
import json
from datetime import datetime
import boto3


# Load the configuration from the JSON file
with open('config.json') as file:
    config = json.load(file)

server = config['server']
database = config['database']
username = config['username']
password = config['password']
tables = config['tables']
s3_bucket = config['s3_bucket']

#Establish connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

# Create a S3 client
s3_client = boto3.client('s3')

# Iterate over the tables and fetch data
for table in tables:
    query = f'SELECT * FROM {table}'
    df = pd.read_sql(query, conn)

    # Get the current datetime
    current_datetime = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save the data to csv file
    csv_filename = f'{table.replace(".", "_")}_{current_datetime}.csv'
    df.to_csv(csv_filename, index=False)

    # Upload the file to S3
    s3_client.upload_file(csv_filename, s3_bucket, csv_filename)

# Close the connection
conn.close()