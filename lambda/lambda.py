import json
import boto3
import os
import time
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    sns = boto3.client('sns')
    table = dynamodb.Table('Contacts')
    unixtime = int(time.time())
    body = json.loads(event['body'])
    headers = event['headers']
    response = sns.publish(
        TopicArn= os.environ['topicArn'],
        Subject=body['name'] +" "+body['email'],
        Message=body['message'])
    table.put_item(
        Item={
            'timestamp':str(unixtime),
            'ip':headers['X-Forwarded-For'],
            'user-agent': headers['User-Agent'],
            'email':body['email'],
            'name':body['name'],
            'message':body['message']
        }    
    )
    callback = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*"
        },
        "body": json.dumps(event)
    }
    return callback
