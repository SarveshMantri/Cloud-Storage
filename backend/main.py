from fastapi import FastAPI, HTTPException, UploadFile, File, status
from s3_upload import s3_upload
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def home():
    return "Welcome to my first FastAPI Application"


@app.get("/front")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/upload" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


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
            status_code=status.HTTP_400_BAD_REQUEST, detail="Something went wrong"
        )
