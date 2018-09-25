# -*- coding: utf-8 -*-
"""
新北市公共自行車即時資訊
主要欄位說明： sno：站點代號、 sna：場站名稱(中文)、 tot：場站總停車格、 
sbi：場站目前車輛數量、 sarea：場站區域(中文)、 mday：資料更新時間、 lat：緯度、 lng：經度、 
ar：地址(中文)、 sareaen：場站區域(英文)、 snaen：場站名稱(英文)、 aren：地址(英文)、 
bemp：空位數量、 act：全站禁用狀態 
"""
import csv
with open('E1-2-2-1-input.csv','r',encoding = 'utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        print(row[0]+" "+row[1]+" "+row[3]+" "+row[5]+" "+row[12])
