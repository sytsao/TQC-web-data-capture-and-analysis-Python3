# -*- coding: utf-8 -*-
"""
'E1-1-2-2-input.pdf'為國人全民健康保險就醫疾病資訊
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
readFile = 'E1-1-2-2-input.pdf'
pdfFileReader = PdfFileReader(readFile,strict=False)  # 或者這個方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
documentInfo = pdfFileReader.getDocumentInfo()
outFile = 'E1-1-2-3-output.pdf'
pdfFileWriter = PdfFileWriter()
numPages = pdfFileReader.getNumPages()
if numPages > 3:
        # 從第3頁之後的頁面，輸出到一個新的檔中，即分割文檔
    for index in range(3, numPages):
        pageObj = pdfFileReader.getPage(index)
        pdfFileWriter.addPage(pageObj)
        # 添加完每頁，再一起保存至檔中
    pdfFileWriter.write(open(outFile, 'wb'))



