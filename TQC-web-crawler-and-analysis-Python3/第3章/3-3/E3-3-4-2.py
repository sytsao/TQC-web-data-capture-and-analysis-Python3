# -*- coding: utf-8 -*-
"""
環保署每小時提供各測站之空氣品質指標（AQI），主要欄位：SiteName(測站名稱)、County(縣市)、
AQI(空氣品質指標)、Pollutant(空氣污染指標物)、Status(狀態)、SO2(二氧化硫(ppb))、
CO(一氧化碳(ppm))、CO_8hr(一氧化碳8小時移動平均(ppm))、O3(臭氧(ppb))、
O3_8hr(臭氧8小時移動平均(ppb))、PM10(懸浮微粒(μg/m3))、PM2.5(細懸浮微粒(μg/m3))、
NO2(二氧化氮(ppb))、NOx(氮氧化物(ppb))、NO(一氧化氮(ppb))、WindSpeed(風速(m/sec))、
WindDirec(風向(degrees))、PublishTime(資料建置日期)、
PM2.5_AVG(細懸浮微粒移動平均值(μg/m3))、PM10_AVG(懸浮微粒移動平均值(μg/m3))、
Latitude(經度)、Longitude(緯度)
"""
import json
import pandas as pd
with open("AQI.json",encoding = 'utf8') as file:
    data = json.load(file)
df = pd.DataFrame(data)
print(df)
df1=df.sort_values(by="AQI", ascending=False)
print('以AQI遞減排序')
print(df1['AQI'])
print(df1.groupby("County").count()["SiteName"])
df2=df1['AQI']
print(df2.describe())

