# -*- coding: utf-8 -*-
"""
某市場2017年全年毛豬交易行情資料，主要欄位：
total_amt(成交頭數-總數)、average_weight(成交頭數-平均重量)、average_price(成交頭數-平均價格)
"""
import pandas as pd

df1 = pd.read_csv('2017pig.csv',encoding="utf-8", sep=",")
df1.columns = [ 'total_amt', 'average_weight', 'average_price']
print(df1.describe())
print(df1.average_price.max())
print(df1.sort_values("average_price", ascending=False).head(5))
print(df1[df1.average_price>90])
print('以average_price遞減排序')
print(df1['average_price'])
print()

print('最後三筆的資料')
print(df1.tail(3))
print()