# -*- coding: utf-8 -*-
"""
新北市公共自行車即時資訊主要欄位說明： sno：站點代號、 sna：場站名稱(中文)、 tot：場站總停車格、 
sbi：場站目前車輛數量、 sarea：場站區域(中文)、 mday：資料更新時間、 lat：緯度、 lng：經度、 
ar：地址(中文)、 sareaen：場站區域(英文)、 snaen：場站名稱(英文)、 aren：地址(英文)、 
bemp：空位數量、 act：全站禁用狀態 
"""

import json
import csv

with open("GE1-1-input.json",encoding = 'utf8') as file:
    data = json.load(file)

with open("GE1-1-output.csv", "w",encoding = 'utf8') as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['sno'], item['sna'],item['tot']])