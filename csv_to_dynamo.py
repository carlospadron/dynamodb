import boto3
import pandas as pd
import os
from decimal import Decimal

# Initialize a session using Amazon DynamoDB
session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('REGION_NAME', 'eu-west-2')
)

# Initialize DynamoDB resource
dynamodb = session.resource('dynamodb')

# Specify the table
table = dynamodb.Table('os_open_uprn')

# Read CSV file
data = pd.read_csv('osopenuprn_202404.csv')
data.columns = data.columns.str.lower()
data = data.to_dict(orient='records')


# Convert float values to Decimal
def convert_floats_to_decimals(item):
    for key, value in item.items():
        if isinstance(value, float):
            item[key] = Decimal(str(value))
    return item

with table.batch_writer() as writer:
    n = 0
    for row in data:
        print(f"Writing record {n} to DynamoDB table.")
        row = convert_floats_to_decimals(row)
        writer.put_item(Item=row)
        n += 1
    

print("CSV data has been written to DynamoDB table.")
#14:54