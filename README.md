# SQL to S3 Data Exporter

This Python script connects to a SQL Server, fetches data from specified tables, saves the data into CSV files, and uploads the CSV files to an Amazon S3 bucket.

## Prerequisites

- Python 3.x
- `pandas` library
- `boto3` library
- `sqlalchemy` library
- `python-dotenv` library
- ODBC Driver 17 for SQL Server

## Installation

1. Install the required Python libraries:
    ```sh
    pip install pyodbc pandas boto3 sqlalchemy python-dotenv
    ```

2. Ensure you have ODBC Driver 17 for SQL Server installed. You can download it from [Microsoft's official website](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server).

## Configuration

1. Create a `.env` file in the same directory as the script with the following content:
    ```env
    STAGE=dev
    DEV_SERVER=your_dev_server_name
    DEV_DATABASE=your_dev_database_name
    DEV_S3_BUCKET=your_dev_s3_bucket_name

    TST_SERVER=your_test_server_name
    TST_DATABASE=your_test_database_name
    TST_S3_BUCKET=your_test_s3_bucket_name

    PRD_SERVER=your_prod_server_name
    PRD_DATABASE=your_prod_database_name
    PRD_S3_BUCKET=your_prod_s3_bucket_name
    ```

2. Replace the placeholders with your actual SQL Server details, table names, and S3 bucket name.

## Usage

1. Set the `STAGE` environment variable to the appropriate stage (development, testing, production).

### On Windows (Command Prompt):
    ```sh
    set STAGE=dev
    python sqltos3.py
    ```

### On Windows (PowerShell):
    ```sh
    $env:STAGE="dev"
    python sqltos3.py
    ```

### On macOS/Linux:
    ```sh
    export STAGE=development
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
Saving data to CSV file: csv/Person_Person_20231010_123456.csv
Uploading CSV file to S3 bucket: your_s3_bucket_name
Fetching data from table: AnotherTable
Saving data to CSV file: csv/AnotherTable_20231010_123456.csv
Uploading CSV file to S3 bucket: your_s3_bucket_name
Closing connection...