from pydantic import BaseModel
from datetime import datetime


class FileAttributes(BaseModel):
    name: str
    awsName: str
    type: str
    size: float
    date: datetime
