# Medical Data Extraction

A full-stack application that extracts structured data from medical PDF documents using OCR (Optical Character Recognition) and Regex-based parsing. The system supports two document types: **Prescriptions** and **Patient Detail Forms**.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Reference](#api-reference)
- [How It Works](#how-it-works)

---

## Overview

This project automates the extraction of key medical information from scanned PDF documents. It uses **Tesseract OCR** to convert PDF pages into text and then applies **regular expressions** to parse out relevant fields. A **FastAPI** backend exposes a REST endpoint, and a **Streamlit** frontend provides a simple UI for uploading PDFs and viewing extracted data.

---

## Features

- Upload PDF medical documents via a web interface
- OCR-powered text extraction using Tesseract and pdf2image
- Intelligent regex parsing for two document types:
  - **Prescription**: patient name, address, medicines, directions, refills
  - **Patient Details**: patient name, phone number, hepatitis B vaccination status, medical problems
- Image preprocessing with OpenCV for better OCR accuracy
- FastAPI backend with a clean REST API
- Streamlit frontend with side-by-side PDF preview and extracted data
- Jupyter notebooks for exploring parsing and CV concepts

---

## Project Structure

```
medical_Data_Extration/
├── backend/
│   ├── src/
│   │   ├── extractor.py            # Core OCR + dispatch logic
│   │   ├── parser_generic.py       # Base class for all parsers
│   │   ├── parser_prescription.py  # Prescription document parser
│   │   ├── parser_patients_detail.py # Patient details document parser
│   │   └── util.py                 # Image preprocessing utilities
│   ├── notebooks/
│   │   ├── cv_concepts1.ipynb      # OpenCV concepts exploration
│   │   ├── prescription_parser1.ipynb
│   │   └── pd_parser1.ipynb
│   ├── resources/                  # Sample PDF files for testing
│   ├── main.py                     # FastAPI application entry point
│   └── requirements.txt            # Backend Python dependencies
├── frontend/
│   └── main.py                     # Streamlit UI application
└── README.md
```

---

## Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Backend   | Python, FastAPI, Uvicorn          |
| OCR       | Tesseract OCR, pdf2image, Poppler |
| CV        | OpenCV (cv2), NumPy               |
| Parsing   | Python re (Regular Expressions)   |
| Frontend  | Streamlit, Requests               |

---

## Prerequisites

Before running the project, install the following system-level dependencies:

### 1. Tesseract OCR
- **Windows**: Download from [UB Mannheim Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) and install to `C:\Program Files\Tesseract-OCR\`
- **Linux**: `sudo apt install tesseract-ocr`
- **macOS**: `brew install tesseract`

### 2. Poppler (PDF rendering)
- **Windows**: Download from [poppler releases](https://github.com/oschwartz10612/poppler-windows/releases/) and extract to `C:\poppler-24.08.0\`
- **Linux**: `sudo apt install poppler-utils`
- **macOS**: `brew install poppler`

---

## Installation

### 1. Clone the repository
```
git clone https://github.com/dharmikebaria/medical_Data_Extration.git
cd medical_Data_Extration
```

### 2. Create and activate a virtual environment
```
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 3. Install Python dependencies
```
pip install -r backend/requirements.txt
```

> **Note for Windows users**: Update the `POPPLER_PATH` and `tesseract_cmd` paths in `backend/src/extractor.py` and `frontend/main.py` to match your local installation directories.

---

## Running the Application

### Start the Backend (FastAPI)
```
cd backend
uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`

### Start the Frontend (Streamlit)
Open a new terminal:
```
cd frontend
streamlit run main.py
```
The UI will open at `http://localhost:8501`

---

## API Reference

### POST /extract_from_doc

Extracts structured data from an uploaded PDF file.

**Form Parameters:**

| Parameter     | Type   | Description                                       |
|---------------|--------|---------------------------------------------------|
| `file_format` | string | Document type: `prescription` or `patient_details`|
| `file`        | file   | The PDF file to process                           |

**Response for `prescription`:**
```json
{
  "patient_name": "Marta Sharapova",
  "patient_address": "9 tennis court, new Russia, DC",
  "medicines": "Prednisone 20 mg\nLialda 2.4 gram",
  "directions": "Prednisone, Taper 5 mg every 3 days...",
  "refills": "3"
}
```

**Response for `patient_details`:**
```json
{
  "patient_name": "Kathy Crawford",
  "phone_number": "(737) 988-0851",
  "hepatitis_b_vaccination": "No",
  "medical_problems": "Migraine"
}
```

---

## How It Works

1. **Upload**: The user uploads a PDF via the Streamlit UI and selects the document type.
