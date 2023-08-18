import boto3
from accessKeys import access_key_id, secret_access_key

s3 = boto3.client(
    "s3", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key
)


async def s3_upload():
    try:
        response = s3.list_buckets()
        print("Existing buckets:")
        for bucket in response["Buckets"]:
            print(f'  {bucket["Name"]}')
    except Exception as e:
        print(f"Something went wrong : {e}")
