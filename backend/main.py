from fastapi import FastAPI, HTTPException, UploadFile, status
from s3_upload import s3_upload

app = FastAPI()


@app.get("/")
def home():
    return "Welcome to my first FastAPI Application"


@app.post("/upload")
async def upload_files(file: UploadFile):
    if not file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No file found"
        )
    await s3_upload()
    return {"name": file.filename}
