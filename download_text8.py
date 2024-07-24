# download_text8.py
import requests
import zipfile
import os

# Download the text8 dataset
url = "http://mattmahoney.net/dc/text8.zip"
dataset_path = 'text8.zip'
text8_path = 'text8'

if not os.path.exists(dataset_path):
    r = requests.get(url, stream=True)
    with open(dataset_path, "wb") as f:
        f.write(r.content)

if not os.path.exists(text8_path):
    with zipfile.ZipFile(dataset_path, "r") as zip_ref:
        zip_ref.extractall(".")
