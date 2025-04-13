from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from extractor import extract
import uuid
import os

app = FastAPI()

UPLOAD_FOLDER = "../uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # ensure the folder exists

@app.post("/extract_from_doc")
def extract_from_doc(
    file_format: str = Form(...),
    file: UploadFile = File(...)
):
    # Save uploaded file temporarily
    file_path = os.path.join(UPLOAD_FOLDER, str(uuid.uuid4()) + ".pdf")

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    try:
        data = extract(file_path, file_format)
    except Exception as e:
        data = {'error': str(e)}

    if os.path.exists(file_path):
        os.remove(file_path)

    return data

# Only runs if you execute this file directly (not needed if running uvicorn externally)
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
