import boto3

import uuid

s3_resource = boto3.resource('s3')


def create_bucket_name(bucket_prefix):
	return ''.join([bucket_prefix, str(uuid.uuid4())])

create_bucket_name("mybucket323232")