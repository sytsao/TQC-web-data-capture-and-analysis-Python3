# -*- coding: utf-8 -*-
import PyPDF2
pdfFiles = [" E1-1-1-1-out0.pdf"," E1-1-1-1-out1.pdf"," E1-1-1-1-out2.pdf"]
pdfWriter = PyPDF2.PdfFileWriter() 
pdfOutput = open('E1-1-2-4-comb.pdf','wb')
for fileName in pdfFiles:
    pdfReader = PyPDF2.PdfFileReader(open(fileName,'rb'))   
    for pageNum in range(pdfReader.numPages):
        print(pdfReader.getPage(pageNum))
        pdfWriter.addPage(pdfReader.getPage(pageNum))  
pdfWriter.write(pdfOutput)        
pdfOutput.close()



