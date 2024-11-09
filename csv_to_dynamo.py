import boto3
import csv
import os

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
with open('osopenuprn_202404.csv', mode='r', encoding='utf-8-sig') as file:
    csv_reader = csv.DictReader(file)
    n = 0
    for row in csv_reader:
        print(n)
        # Write each row to DynamoDB
        row = {k.lower(): v for k, v in row.items()}
        row['uprn'] = int(row['uprn'])
        #print(row)
        table.put_item(Item=row)
        n += 1


print("CSV data has been written to DynamoDB table.")