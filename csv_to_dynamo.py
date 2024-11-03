import boto3
import csv

# Initialize a session using Amazon DynamoDB
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='YOUR_REGION'
)

# Initialize DynamoDB resource
dynamodb = session.resource('dynamodb')

# Specify the table
table = dynamodb.Table('YourTableName')

# Read CSV file
with open('yourfile.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Write each row to DynamoDB
        table.put_item(Item=row)

print("CSV data has been written to DynamoDB table.")