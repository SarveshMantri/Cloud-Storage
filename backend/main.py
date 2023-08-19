from fastapi import FastAPI, HTTPException, UploadFile, File, status
from fastapi.middleware.cors import CORSMiddleware
from models import FileAttributes
from s3_upload import s3_upload

from database import fetch_all_files

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Welcome to my first FastAPI Application"


@app.post("/upload")
async def upload_files(files: list[UploadFile] = File(...)):
    if not files:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No file found"
        )

    response = await s3_upload(files)
    if response:
        return {"names": [file.filename for file in files]}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong while uploading the files to S3 bucket.",
        )


@app.get("/all-file-attributes")
async def get_all_file_attributes() -> list[FileAttributes] | None:
    response = None
    try:
        response = await fetch_all_files()
    except Exception as e:
        print(e)
        return None
    return response
