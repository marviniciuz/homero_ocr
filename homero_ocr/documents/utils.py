import pytesseract
from PIL import Image
import fitz  # PyMuPDF
from gtts import gTTS
import os
from django.conf import settings


def extract_text_from_file(file_path):
    text = ""
    if file_path.lower().endswith(".pdf"):
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()
        doc.close()
    else:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image, lang="por")
    return text.strip()


def text_to_speech(text, output_path, lang="pt"):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_path)
    return output_path

