from models import FileAttributes
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

database = client.FileAttributes
collection = database.files


async def fetch_all_files():
    files = []
    cursor = collection.find({})
    async for document in cursor:
        files.append(FileAttributes(**document))
    return files


async def create_file_entry(file):
    document = file
    result = await collection.insert_one(document)
