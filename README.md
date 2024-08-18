# Image_and_PDF_to_Speech_Conversion_System

**Project Overview**
This project provides a set of Python scripts that convert text from PDF files and images into speech. The conversion is handled using libraries such as PyPDF2, pyttsx3, and gTTS (Google Text-to-Speech). The project includes two main functionalities:

**PDF to Speech Conversion:** Extracts text from a PDF file and converts it to speech.
**Image to Speech Conversion:** Extracts text from an image and converts it to speech.
Prerequisites
Before running the scripts, ensure you have the following libraries installed:

**PyPDF2:** For extracting text from PDF files.
pip install PyPDF2
**pyttsx3:** For converting text to speech using offline text-to-speech synthesis.
pip install pyttsx3
**gTTS (Google Text-to-Speech):** For converting text to speech using Google's text-to-speech engine.
pip install gTTS
**pytesseract:** For extracting text from images.
pip install pytesseract
**PIL (Python Imaging Library):** Required for image processing.
pip install pillow
**Usage**
PDF to Speech Conversion
The pdfconverter() function allows you to convert text from a PDF file to speech. It provides three options:

Read the entire PDF: Convert all text from the PDF to speech.
Read a specific range of pages: Convert text from a specified range of pages to speech.
Read a specific page: Convert text from a single page to speech.
Make sure your PDF file is named file.pdf and located in the same directory as the script.

Image to Speech Conversion
The imageconverter() function extracts text from an image and converts it to speech. The image should be named imagetext.jpg and be located in the same directory as the script.

**How to Run**
Place your file.pdf and/or imagetext.jpg in the project directory.
Run the converter script in your Python environment.
Follow the on-screen instructions to choose the conversion mode.
**Dependencies**
Ensure that Tesseract-OCR is installed on your system for the image conversion to work. You can download it from Tesseract GitHub.
