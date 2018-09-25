# -*- coding: utf-8 -*-
"""
新北市公共自行車即時資訊主要欄位說明： sno：站點代號、 sna：場站名稱(中文)、 tot：場站總停車格、 
sbi：場站目前車輛數量、 sarea：場站區域(中文)、 mday：資料更新時間、 lat：緯度、 lng：經度、 
ar：地址(中文)、 sareaen：場站區域(英文)、 snaen：場站名稱(英文)、 aren：地址(英文)、 
bemp：空位數量、 act：全站禁用狀態 
"""

import xml.etree.ElementTree as ET
import csv
tree = ET.parse("GE1-5-input.xml")
root = tree.getroot()

ubikefile = open("GE1-5-output.csv", "w",encoding = 'utf8') 
csvwriter = csv.writer(ubikefile)

for row in root:
	ubike = []
	sno = row.find('sno').text
	ubike.append(sno)
	sna = row.find('sna').text
	ubike.append(sna)
	tot = row.find('tot').text
	ubike.append(tot)
	csvwriter.writerow(ubike)
ubikefile.close()
