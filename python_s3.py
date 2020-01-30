import boto3



def create_bucket(bucket_name):
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket=bucket_name)
   

create_bucket(bucket_name="mydemo123bucketunique")
print(create_bucket)
