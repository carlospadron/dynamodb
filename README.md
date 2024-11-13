# dynamodb
Notes on using dynamo db

# run locally 

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb

# Notes
- dynamodb can handle very large of I/O requests
- Inserts can be done in batches but anyway can be slow if the uploader is not using parallel processes
- Free tier gets consumed very fast
- For analytics, Big Query is better (allows sql, can read CSV faster)
- Dynamodb is better suited for mobile apps where many devices are reading and writing