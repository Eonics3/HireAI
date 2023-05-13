# importing required modules
from PyPDF2 import PdfReader
  

def readResume():
    # creating a pdf reader object
    reader = PdfReader('resume.pdf')
    
    # printing number of pages in pdf file

    text = ""

    for i in range(len(reader.pages)):
        text+=((reader.pages[i]).extract_text())
    
    f = open("resume.txt", "w")
    f.write(text)
    f.close()
