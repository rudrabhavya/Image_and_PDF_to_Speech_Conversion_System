# this is to import tesseract module for getting the text from the image
import pytesseract
# PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities
from PIL import Image
# this is to import gTTS for the text to speech conversion
from gtts import gTTS
# the OS module in Python provides functions for interacting with the operating system
import os
import pyttsx3
def imageconverter():
    img = Image.open("imagetext.jpg")

# getting text from the image
    text = pytesseract.image_to_string(img)

# storing the text in the file sample.txt
    textfile = open('file.txt', 'w')
    textfile.write(text)
    print("Text is written in file!")
    textfile.close()

# getting the text from the file
    textfile = open('file.txt')
    text = textfile.read()
    print(text)
    lang = 'en'
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()
