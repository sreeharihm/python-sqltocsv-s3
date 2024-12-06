import pandas as pd
import boto3
import os
from sqlalchemy import create_engine
from datetime import datetime
from dotenv import load_dotenv


# Load environment vairalbes from .env file
load_dotenv()

#Get the current stage
stage = os.getenv('STAGE', 'dev')

server = os.getenv(f'{stage}_SERVER')
database = os.getenv(f'{stage}_DATABASE')
s3_bucket = os.getenv(f'{stage}_S3_BUCKET')

#Establish connection
connection_string = f'mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'

# Create sql engine
engine = create_engine(connection_string)

# Create a S3 client
s3_client = boto3.client('s3')

#Fetch all the tables from the database
query = "SELECT TABLE_SCHEMA + '.' + TABLE_NAME AS table_name FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"
tables_df = pd.read_sql(query, connection_string)
tables = tables_df['table_name'].tolist()

# Create the CSV directory if it does not exist
os.makedirs('csv', exist_ok=True)

# Iterate over the tables and fetch data
for table in tables:
    try:
        query = f'SELECT * FROM {table}'
        df = pd.read_sql(query, connection_string)

        # Get the current datetime
        current_datetime = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Save the data to csv file in the 'csv' folder
        csv_filename = f'csv/{table.replace(".", "_")}_{current_datetime}.csv'
        df.to_csv(csv_filename, index=False)

        # Upload the file to S3
        s3_client.upload_file(csv_filename, s3_bucket, csv_filename)
    except Exception as e:
        print(f"Failed to fetch data from the table {table}: {e}")

# Close the connection
engine.dispose()