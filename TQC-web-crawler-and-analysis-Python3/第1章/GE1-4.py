# -*- coding: utf-8 -*-
"""
文化部展覽資訊，主要欄位：
version(發行版本)、UID(唯一辨識碼)、title(活動名稱)、category(活動類別)、
showUnit(演出單位)、descriptionFilterHtml(簡介說明)、discountInfo(折扣資訊)、
imageURL(圖片連結)、masterUnit(主辦單位)、subUnit(協辦單位)、supportUnit(贊助單位)、
otherUnit(其他單位)、webSales(售票網址)、sourceWebPromote(推廣網址)、comment(備註)、
editModifyDate(編輯時間)、sourceWebName(來源網站名稱)、startDate(活動起始日期)、
endDate(活動結束日期)、hitRate(點閱數)、showinfo(活動場次資訊)、time(單場次演出時間)、
location(地址)、locationName(場地名稱)、onSales(是否售票)、
latitude(緯度)、longitude(經度)、Price(售票說明)、endTime(結束時間)
"""

import json
import csv

with open("GE1-4-input.json",encoding = 'utf8') as file:
    data = json.load(file)

with open("GE1-4-output.csv", "w",encoding = 'utf8') as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['title'], item['showUnit'],item['startDate'],item['endDate']])