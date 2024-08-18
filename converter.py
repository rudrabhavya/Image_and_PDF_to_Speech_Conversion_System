#Importing modules imagemain and text speech
import imagetext
import pdftext
#Providing user options to chose
print("1.Image to speech\n2.Pdf to speech")
c=int(input("Enter your choice"))
if c==1:
    #Calling the function imageconverter from imagemain
    imagetext.imageconverter()
else:
    #Calling the function pdfconverter from textspeech
    pdftext.pdfconverter()