# SQL to S3 Data Exporter

This Python script connects to a SQL Server, fetches data from specified tables, saves the data into CSV files, and uploads the CSV files to an Amazon S3 bucket.

## Prerequisites

- Python 3.x
- `pyodbc` library
- `pandas` library
- `boto3` library
- ODBC Driver 17 for SQL Server

## Installation

1. Install the required Python libraries:
    ```sh
    pip install pyodbc pandas boto3
    ```

2. Ensure you have ODBC Driver 17 for SQL Server installed. You can download it from [Microsoft's official website](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server).

## Configuration

1. Create a `config.json` file in the same directory as the script with the following content:
    ```json
    {
        "server": "your_server_name",
        "database": "your_database_name",
        "username": "your_username",
        "password": "your_password",
        "tables": ["Person.Person", "AnotherTable"],
        "s3_bucket": "your_s3_bucket_name"
    }
    ```
    Replace the placeholders with your actual SQL Server details, table names, and S3 bucket name.

## Usage

1. Run the script:
    ```sh
    python sqltos3.py
    ```

2. The script will:
    - Connect to the SQL Server using the provided configuration.
    - Fetch data from the specified tables.
    - Save the data into CSV files with the current datetime in the filename.
    - Upload the CSV files to the specified S3 bucket.

## Example

Here is an example of the script's output:
```sh
Connecting to SQL Server...
Fetching data from table: Person.Person
Saving data to CSV file: Person_Person_20231010_123456.csv
Uploading CSV file to S3 bucket: your_s3_bucket_name
Fetching data from table: AnotherTable
Saving data to CSV file: AnotherTable_20231010_123456.csv
Uploading CSV file to S3 bucket: your_s3_bucket_name
Closing connection...