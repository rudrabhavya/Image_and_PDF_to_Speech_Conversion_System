import PyPDF2
import pyttsx3
from gtts import gTTS
import os
from gtts import gTTS
import PyPDF2
def pdfconverter():
    pdf_File = open('file.pdf', 'rb') 
    pdf_Reader = PyPDF2.PdfReader(pdf_File)
    count = len(pdf_Reader.pages) # counts number of pages in pdf
    print(count)
    textList = []
    print("1.Read full pdf\n2.Read from range(m,n)\n3.read nth page")
    n=int(input("Enter choice"))
    if n==1:
        for i in range(count):
            try:
                page = pdf_Reader.pages[i]    
                textList.append(page.extract_text())
            except:
                pass
        textString = " ".join(textList)
        print(textString)
        speak = pyttsx3.init()
        speak.say(textString)
        speak.runAndWait()
    elif n==2:
        m=int(input("Enter m"))
        l=int(input("Enter n"))
        for i in range(m,l+1):
            try:
                page = pdf_Reader.pages[i-1]    
                textList.append(page.extract_text())
            except:
                pass
        textString = " ".join(textList)
        print(textString)
        speak = pyttsx3.init()
        speak.say(textString)
        speak.runAndWait()
    else:
        k=int(input("Enter n"))
        try:
                page = pdf_Reader.pages[k-1]    
                textList.append(page.extract_text())
        except:
                pass
        textString = " ".join(textList)
        print(textString)
        speak = pyttsx3.init()
        speak.say(textString)
        speak.runAndWait()
