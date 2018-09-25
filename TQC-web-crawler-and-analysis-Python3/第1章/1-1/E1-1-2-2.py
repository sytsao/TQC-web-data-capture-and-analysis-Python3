# -*- coding: utf-8 -*-
"""
'E1-1-2-2-input.pdf'為國人全民健康保險就醫疾病資訊
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
readFile = 'E1-1-2-2-input.pdf'
pdfFileReader = PdfFileReader(readFile,strict=False)  # 或者這個方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
documentInfo = pdfFileReader.getDocumentInfo()
outFile = 'E1-1-2-2-output.pdf'
pdfFileWriter = PdfFileWriter()
numPages = pdfFileReader.getNumPages()
for index in range(0, numPages):
    pageObj = pdfFileReader.getPage(index)
    pdfFileWriter.addPage(pageObj)  # 根據每頁返回的 PageObject,寫入到文件
    pdfFileWriter.write(open(outFile, 'wb'))
pdfFileWriter.addBlankPage()   # 在檔的最後一頁寫入一個空白頁,保存至檔中
pdfFileWriter.write(open(outFile,'wb'))


