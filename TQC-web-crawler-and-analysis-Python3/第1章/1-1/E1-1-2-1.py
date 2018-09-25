# -*- coding: utf-8 -*-
"""
'E1-1-2-1-input.pdf'為行政院環境保護署及地方政府 公告 118 條河川  
「水區、體分類」 「水區、體分類」 「水區、體分類」 「水區、體分類」 摘要 彙總 表
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
readFile = 'E1-1-2-1-input.pdf'
pdfFileReader = PdfFileReader(readFile)  # 或者這個方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
documentInfo = pdfFileReader.getDocumentInfo()
print('documentInfo = %s' % documentInfo)
pageLayout = pdfFileReader.getPageLayout()
print('pageLayout = %s ' % pageLayout)
pageMode = pdfFileReader.getPageMode()
print('pageMode = %s' % pageMode)
xmpMetadata = pdfFileReader.getXmpMetadata()
print('xmpMetadata  = %s ' % xmpMetadata)
pageCount = pdfFileReader.getNumPages()
print('pageCount = %s' % pageCount)
for index in range(0, pageCount):
    pageObj = pdfFileReader.getPage(index)
    print('index = %d , pageObj = %s' % (index, type(pageObj)))  # <class 'PyPDF2.pdf.PageObject'>
    pageNumber = pdfFileReader.getPageNumber(pageObj)
    print('pageNumber = %s ' % pageNumber)
