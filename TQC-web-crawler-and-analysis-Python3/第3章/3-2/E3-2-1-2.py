# -*- coding: utf-8 -*-
"""
某市場2017年全年毛豬交易行情資料，主要欄位：
total_amt(成交頭數-總數)、average_weight(成交頭數-平均重量)、average_price(成交頭數-平均價格)
"""
import numpy as np
nf1 = np.genfromtxt('2017pig.csv',delimiter=',',skip_header=1)
print("市場全年成交最高平均重量"+str(nf1[:,1].max(axis=0)))
print("市場全年成交最低平均價"+str(nf1[:,2].min(axis=0)))
print("市場全年總成交頭數"+str(nf1[:,0].sum(axis=0)))
total_sales=(nf1[:,0]*nf1[:,1]*nf1[:,2])
print("市場全年總成交金額"+str(total_sales.sum(axis=0)))
print("市場全年成交平均每頭金額"+str(total_sales.sum(axis=0)/nf1[:,0].sum(axis=0)))
