import json
import boto3

# Dummy token
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"

# Dummy AWS keys
AWS_ACCESS_KEY_ID = "AQASDMNXCVKJYHUS"
AWS_SECRET_ACCESS_KEY = "YJjkhasdknbmnbHkasdmbnJHZJKH"

# Create a Boto3 client for DynamoDB
dynamodb = boto3.client("dynamodb", aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Create a table to store the to do items
dynamodb.create_table(
    TableName="ToDoItems",
    AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
    KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
    ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
)

# Create a function to add a new to do item
def add_todo_item(item):
    dynamodb.put_item(TableName="ToDoItems", Item=item)

# Create a function to get all to do items
def get_all_todo_items():
    response = dynamodb.scan(TableName="ToDoItems")
    return response["Items"]

# Create a function to mark a to do item as complete
def mark_todo_item_as_complete(id):
    dynamodb.update_item(
        TableName="ToDoItems",
        Key={"id": {"S": id}},
        UpdateExpression="SET completed = :completed",
        ExpressionAttributeValues={":completed": {"BOOL": True}},
    )

# Add a new to do item
add_todo_item({"id": "1", "text": "Buy groceries"})

# Get all to do items
todo_items = get_all_todo_items()

# Print all to do items
for todo_item in todo_items:
    print(todo_item["text"])

# Mark a to do item as complete
mark_todo_item_as_complete("1")
