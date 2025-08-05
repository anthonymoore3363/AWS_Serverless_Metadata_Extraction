# Serverless Metadata Extraction (AWS CloudFormation)

This project showcases an event-driven, serverless architecture built with AWS CloudFormation to extract and store file metadata from S3 uploads into DynamoDB.

## Features

- S3 bucket with versioning and EventBridge notifications
- Lambda function written in Python (triggered on S3 uploads)
- DynamoDB table with TTL and on-demand billing
- IAM role for secure access
- EventBridge rule to connect events
- Infrastructure-as-Code using CloudFormation

## Skills Demonstrated

- AWS infrastructure and identity/security constructs
- CloudFormation for repeatable infrastructure deployment
- Event-driven design using AWS Lambda and S3
- IAM policies and permission management
- Use of DeletionPolicy for data retention

## Deployment

1. Upload your zipped `index.py` to an S3 bucket.
2. Launch the stack via CloudFormation, providing:
   - `LambdaS3BucketName`
   - `LambdaS3Key`
3. View logs in CloudWatch and data in DynamoDB after uploading a file to S3.
