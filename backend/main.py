from fastapi import FastAPI, Form, UploadFile, File
from src.extractor import extract
import uuid
import os

app = FastAPI()

UPLOAD_FOLDER = "../../uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # ensure the folder exists

@app.post("/extract_from_doc")
def extract_from_doc(
    file_format: str = Form(...),
    file: UploadFile = File(...)
):
    # Save uploaded file temporarily
    file_path = os.path.join(UPLOAD_FOLDER, str(uuid.uuid4()) + ".pdf")

    print("============= FILE PATH ===============", file_path)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    try:
        data = extract(file_path, file_format)
        print("============= DATA ===============", data)
    except Exception as e:
        data = {'error': str(e)}

    if os.path.exists(file_path):
        os.remove(file_path)

    return data
