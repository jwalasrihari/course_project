import pyttsx3
import PyPDF2
import tkinter.filedialog

def text_to_speech():
    
    file=tkinter.filedialog.askopenfilename()
    
    book=open(file,'rb')
    pdfReader=PyPDF2.PdfFileReader(book)
    pages=pdfReader.numPages
    print("number of pages",pages)
    speaker=pyttsx3.init()
    page=pdfReader.getPage(6)
    text=page.extractText()
    print("speaking...")
    speaker.say(text)
    speaker.runAndWait()
    
#text_to_speech()