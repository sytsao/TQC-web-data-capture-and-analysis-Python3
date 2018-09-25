# -*- coding: utf-8 -*-
"""
網路抓取的網頁與本地Html均為電腦技能基金會首頁
"""
import pdfkit
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
#網路抓取網頁轉換成pdf
pdfkit.from_url("https://www.csf.org.tw/main/index.asp",  " E1-1-1-1-out0.pdf",configuration=config)
#字串轉換成pdf
pdfkit.from_string('Hello World!', ' E1-1-1-1-out1.pdf',configuration=config)
#本地Html轉換成pdf
pdfkit.from_file("電腦技能基金會.html", ' E1-1-1-1-out2.pdf',configuration=config)

