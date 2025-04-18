from pdf2image import convert_from_path
import pytesseract
from src import util

from src.parser_prescription import PrescriptionParser
from src.parser_patients_detail import PatientDetailsParser

POPPLER_PATH = r'C:\poppler-21.02.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract(file_path, file_format):
    # step 1: extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''

    if len(pages)>0:
        page = pages[0]
        processed_image = util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    # step 2: extract fields from text
    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()
    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid document format: {file_format}")

    return extracted_data
#
# if __name__ == '__main__':
#     data = extract('../resources/prescription/pre_2.pdf', 'prescription')
#     print(data)