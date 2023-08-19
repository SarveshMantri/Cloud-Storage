import boto3
from accessKeys import access_key_id, secret_access_key
from fastapi import UploadFile

__s3 = boto3.client(
    "s3", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key
)

__bucket = "cloudstorageproject"


async def s3_upload(files: list[UploadFile]) -> bool:
    try:
        for file in files:
            __s3.upload_fileobj(file.file, __bucket, file.filename)
    except Exception as e:
        print(f"Something went wrong : {e}")
        return False
    return True
