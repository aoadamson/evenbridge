import boto3
import json

# Create a Lambda client using the default credentials
lambda_client = boto3.client('lambda')

# Set the name of the Lambda function to invoke
function_name = 'InfraStack-MyFunction3BAA72D1-oOQ7ax4Dp3L0'

# Define the input event as a dictionary
event = {'operation': 'write', 'name': 'austin', 'value': 'aviation'}

# Invoke the Lambda function with the input event
response = lambda_client.invoke(FunctionName=function_name, Payload=json.dumps(event))

# Parse the response from the Lambda function
response_payload = json.loads(response['Payload'].read())

# Print the response payload
print(response_payload)
