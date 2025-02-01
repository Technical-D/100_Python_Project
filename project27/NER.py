import requests
from dotenv import load_dotenv
import os
import fitz
import json
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
HEADERS = {"Authorization": f"Bearer {os.getenv('API_Key')}"}

def get_ner(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF file using PyMuPDF
    """
    doc = fitz.open(file_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

text = extract_text_from_pdf(r"D:\study material\resume\Dheeraj_Gupta1.1.pdf")
ner_result = get_ner(text)
print(json.dumps(ner_result))