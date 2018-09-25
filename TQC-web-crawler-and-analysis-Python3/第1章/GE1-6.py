# -*- coding: utf-8 -*-
"""
中華郵政公司縣市鄉鎮中英對照檔
主要欄位說明： 欄位1：郵遞區號、 欄位2：縣市鄉鎮(中文)、 欄位3：縣市鄉鎮(英文)
"""

import xml.etree.ElementTree as ET
import csv
tree = ET.parse("GE1-6-input.xml")
root = tree.getroot()

Countyfile = open("GE1-6-output.csv", "w",encoding = 'utf8') 
csvwriter = csv.writer(Countyfile)

for row in root:
	County = []
	pno = row.find('欄位1').text
	County.append(pno)
	cname = row.find('欄位2').text
	County.append(cname)
	ename = row.find('欄位3').text
	County.append(ename)
	csvwriter.writerow(County)
Countyfile.close()
