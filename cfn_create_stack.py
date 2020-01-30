import boto3 
from pathlib import Path

client = boto3.client('cloudformation')

response = client.create_stack(
    StackName='myboto3cfnstack',
    TemplateBody='https://hunaidsfolder.s3.amazonaws.com/userdata.yaml',
    Parameters=[
        {
            'ParameterKey': 'SSHkey',
            'ParameterValue': 'ohio_rivia',
           
        },
    ],
 
   
    TimeoutInMinutes=5
    # NotificationARNs=[
    #     'string',
    # ],
    # Capabilities=[
    #     'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
    # ],
    
  
    
    
)