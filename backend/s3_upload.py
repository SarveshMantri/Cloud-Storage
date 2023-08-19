import boto3
from accessKeys import access_key_id, secret_access_key
from database import create_file_entry
from datetime import datetime
from fastapi import UploadFile
from uuid import uuid4


__s3 = boto3.client(
    "s3", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key
)

__bucket = "cloudstorageproject"


async def s3_upload(files: list[UploadFile]) -> bool:
    try:
        for file in files:
            content = await file.read()
            size = len(content) / 1024
            awsName = f"{uuid4()}-{file.filename}"
            await file.seek(0)
            __s3.upload_fileobj(file.file, __bucket, awsName)
            file_dict = {
                "name": file.filename,
                "awsName": awsName,
                "type": file.content_type,
                "size": size,
                "date": datetime.utcnow(),
            }
            await create_file_entry(file_dict)
    except Exception as e:
        print(f"Something went wrong : {e}")
        return False
    return True
