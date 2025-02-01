import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
HEADERS = {"Authorization": f"Bearer {os.getenv('API_Key')}"}

def get_ner(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

text = "Wolfgang lives in Berlin."
result = get_ner(text)
print(result)