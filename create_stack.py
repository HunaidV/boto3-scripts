import boto3


def stack_creation(stack_name,templateUrl,parameters,capabilities,onfailure):
	client = boto3.client('cloudformation')

	response = client.create_stack(
		StackName = stack_name,
		TemplateURL = templateUrl,
		Parameters = parameters,
		OnFailure = onfailure

		)

stack_name = "cfntorunuserdata"
templateUrl = "https://s3.amazonaws.com/hunaidsfolder/userdata.template"
parameters = [
        {
            'ParameterKey': 'SSHkey',
            'ParameterValue': 'california_rivia'
            
        },
    ]

capabilities = 'CAPABILITY_IAM'
onfailure ='DO_NOTHING'

stack_creation(stack_name,templateUrl,parameters,capabilities,onfailure)
