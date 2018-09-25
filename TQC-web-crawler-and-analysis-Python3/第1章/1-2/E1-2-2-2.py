# -*- coding: utf-8 -*-
"""
全國環境輻射偵測即時資訊
主要欄位說明： 監測站,監測站(英文),監測值(微西弗/時),時間,GPS經度,GPS緯度 
"""
import csv
with open('E1-2-2-2-input.csv','r',encoding = 'utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        print(row[0]+" "+row[2]+" "+row[3])
