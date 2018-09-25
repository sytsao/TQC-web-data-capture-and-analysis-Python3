# -*- coding: utf-8 -*-

import csv

infn = 'input.csv'                                # 設定來源檔案
outfn = 'output.csv'                               # 設定目的檔案



with open(infn) as csvRFile:                        # 開啟csv檔案進行讀取
    csvReader = csv.reader(csvRFile)                # 將讀入的檔案建立益Reader物件
    listReport = list(csvReader)                    # 將資料轉成串列 
    for row in listReport:                        #將資料輸出
        print(row[0],row[1])
    
    print('----------')

    
with open(outfn, 'w', newline = '') as csvOFile:    # 開啟csv檔案進行寫入 
    csvWriter = csv.writer(csvOFile )                # 建立Writer物件  
    for row in listReport:                          # 將串列寫入
        csvWriter.writerow(row)
    csvWriter.writerow(['花茶','15','12','500'])     # 將新資料寫入
    csvWriter.writerow(['蜜茶','10','9','300'])     # 將新資料寫入

with open(outfn) as csvRFile:                        # 開啟csv檔案進行讀取

    csvReader = csv.reader(csvRFile)                # 將讀入的檔案建立益Reader物件
    listReport = list(csvReader)                    # 將資料轉成串列 
    for row in listReport:                        #將資料輸出
        print(row[0],row[1])


