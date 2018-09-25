# -*- coding: utf-8 -*-
import pdfkit
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
pdfkit.from_url("電腦技能基金會.html", "out0.pdf",configuration=config)
#字串轉換成pdf
pdfkit.from_string('Hello Python!', 'out1.pdf',configuration=config)
import PyPDF2
pdfFiles = ["out0.pdf","out1.pdf","input.pdf"]
pdfWriter = PyPDF2.PdfFileWriter() 
for fileName in pdfFiles:
    pdfReader = PyPDF2.PdfFileReader(open(fileName,'rb'))   
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))   
        pdfOutput = open('combine.pdf','wb')     
pdfWriter.write(pdfOutput)        
pdfOutput.close()
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
def parse():
    fn = open('combine.pdf','rb')
    parser = PDFParser(fn)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize("")
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        resource = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(resource,laparams=laparams)
        interpreter = PDFPageInterpreter(resource,device)
        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for out in layout:
                if hasattr(out,"get_text"):
                    with open('output.txt','a',encoding='utf-8') as f:
                        f.write(out.get_text()+'\n')
if __name__ == '__main__':
	parse()

