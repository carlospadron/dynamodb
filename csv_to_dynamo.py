import boto3
import pandas as pd
import os
from decimal import Decimal

# Initialize a session using Amazon DynamoDB
session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('REGION_NAME', 'eu-west-2')  # Default region fallback
)

# Initialize DynamoDB resource
dynamodb = session.resource('dynamodb')

# Specify the table
table = dynamodb.Table('os_open_uprn')

# Convert float values to Decimal
def convert_floats_to_decimals(item):
    for key, value in item.items():
        if isinstance(value, float):
            item[key] = Decimal(str(value))
    return item

# Read and process CSV file in chunks
chunk_size = 100000
n=0
for chunk in pd.read_csv('osopenuprn_202404.csv', chunksize=chunk_size):
    chunk.columns = chunk.columns.str.lower()
    data = chunk.to_dict(orient='records')
    
    with table.batch_writer() as writer:
        for row in data:
            row = convert_floats_to_decimals(row)
            writer.put_item(Item=row)

    n += chunk_size
    print(f"Processed {n} rows.")

print("CSV data has been written to DynamoDB table.")
#15:26