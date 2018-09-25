# -*- coding: utf-8 -*-
"""
經勞動部會商衛生福利部認可得辦理勞工體格及健康檢查之醫療機構名單
主要欄位說明： 縣市別、醫療機構名稱、醫療機構地址、勞工健檢聯絡人、連絡電話、認可項目及認可期限、備註
"""

import xml.etree.ElementTree as ET
import csv
tree = ET.parse("GE1-7-input.xml")
root = tree.getroot()

Hospitalfile = open("GE1-7-output.csv", "w",encoding = 'utf8') 
csvwriter = csv.writer(Hospitalfile)

for row in root:
	Hospital = []
	pno = row.find('縣市別').text
	Hospital.append(pno)
	cname = row.find('醫療機構名稱').text
	Hospital.append(cname)
	ename = row.find('醫療機構地址').text
	Hospital.append(ename)
	csvwriter.writerow(Hospital)
Hospitalfile.close()
