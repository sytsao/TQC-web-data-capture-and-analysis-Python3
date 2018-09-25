# -*- coding: utf-8 -*-
"""
'E1-1-2-2-input.pdf'為國人全民健康保險就醫疾病資訊
"""
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
def parse():
    fn = open('E1-1-2-2-input.pdf','rb')
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
                    with open('E1-1-3-1-output.txt','a') as f:
                        f.write(out.get_text()+'\n')
if __name__ == '__main__':
	parse()

