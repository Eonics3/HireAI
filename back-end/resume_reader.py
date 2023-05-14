# importing required modules
from PyPDF2 import PdfReader

import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
print("path: ", dir_path)

script_dir = os.path.dirname( __file__ )
# mymodule_dir = os.path.join( script_dir, '..', 'alpha', 'beta' )
sys.path.append( script_dir )
  

def readResume():
    # creating a pdf reader object
    script_dir = os.path.dirname( __file__ )
    # mymodule_dir = os.path.join( script_dir, '..', 'alpha', 'beta' )
    sys.path.append( script_dir )
    fd = open('./resume.pdf', "rb")
    reader = PdfReader('./resume.pdf')
    
    # printing number of pages in pdf file

    text = ""

    for i in range(len(reader.pages)):
        text+=((reader.pages[i]).extract_text())
    
    f = open("resume.txt", "w")
    f.write(text)
    f.close()
