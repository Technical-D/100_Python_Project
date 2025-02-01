import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/microsoft/table-transformer-structure-recognition"
HEADERS = {"Authorization": f"Bearer {os.getenv('API_Key')}"}

def extract_table(image_path):
    with open(image_path, "rb") as img:
        payload = img.read() 
        
    response = requests.post(API_URL, headers={**HEADERS, "Content-Type": "application/octet-stream"}, data=payload)
    return response.json()

image_path = "table-binary.png"
result = extract_table(image_path)

import cv2
import pytesseract
import pandas as pd

# Function to extract text from the bounding boxes
def extract_text_from_region(image, box):
    # Crop the image using the bounding box
    cropped_img = image[box['ymin']:box['ymax'], box['xmin']:box['xmax']]
    
    # Use Tesseract OCR to extract text from the cropped image
    text = pytesseract.image_to_string(cropped_img, config='--psm 6')
    
    return text.strip()

image = cv2.imread(image_path)

# Extract text for columns and rows
columns = []
rows = []

# Extract column headers first (if any)
for item in result:
    if item['label'] == 'table column header':
        column_text = extract_text_from_region(image, item['box'])
        columns.append(column_text)

# Extract rows
for item in result:
    if item['label'] == 'table row':
        row_text = extract_text_from_region(image, item['box'])
        rows.append(row_text)

# Organize the data into a DataFrame
table_data = []
for row in rows:
    row_data = row.split('\n')  
    table_data.append(row_data)

# Create a DataFrame from the extracted table data
df = pd.DataFrame(table_data, columns=columns)
print(df)

# Save the table to a CSV file
df.to_csv('extracted_table.csv', index=False)
