import requests
import pandas as pd
from datetime import datetime
import boto3
from io import StringIO

# It's better to use the default session which will pick up the credentials
# from your environment or AWS credentials file.
# If you need to specify the region, you can pass it to the client creation.
# s3_client = boto3.client('s3', region_name='ap-south-1')  # Replace with your region

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def transform_data(data):
    flattened_data = []
    for fy, records in data.items():
        for record in records:
            record['fy'] = fy
            flattened_data.append(record)
    return pd.DataFrame(flattened_data)

def upload_to_s3(bucket_name, file_name, data):
    csv_buffer = StringIO()
    data.to_csv(csv_buffer, index=False)
    s3_client = boto3.client('s3')
    s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())

def monthly_etl():
    try:
        print("Starting ETL process...")
        api_url = 'https://cea.nic.in/api/power_generation.php'
        data = fetch_data(api_url)
        df = transform_data(data)
        
        if df.empty:
            print("No data fetched or transformed.")
            return
        
        file_name = datetime.now().strftime('%Y-%m-%d.csv')
        bucket_name = 'hemanthkajuluri2'  # Make sure this is the correct bucket name
        
        upload_to_s3(bucket_name, file_name, df)
        print(f"Data uploaded successfully to {bucket_name} with the file name {file_name}")
    except Exception as e:
        print(f"An error occurred during the ETL process: {str(e)}")

if __name__ == "__main__":
    monthly_etl()
