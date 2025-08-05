import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

# Get the DynamoDB table name from the environment variable
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            bucket_name = record['s3']['bucket']['name']
            object_key = record['s3']['object']['key']

            # Get metadata from the object
            response = s3.head_object(Bucket=bucket_name, Key=object_key)
            metadata = {
                'FileID': object_key,
                'Bucket': bucket_name,
                'Size': response['ContentLength'],
                'ContentType': response.get('ContentType', 'unknown'),
                'LastModified': response['LastModified'].isoformat()
            }

            table.put_item(Item=metadata)
            print(f"Metadata saved for {object_key}")

        return {
            'statusCode': 200,
            'body': json.dumps('Metadata processed successfully')
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error processing metadata: {str(e)}")
        }