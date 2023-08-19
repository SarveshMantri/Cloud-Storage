from pydantic import BaseModel
from datetime import datetime


class FileAttributes(BaseModel):
    name: str
    type: str
    size: float
    date: datetime
