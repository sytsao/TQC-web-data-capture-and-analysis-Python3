# -*- coding: utf-8 -*-
import numpy as np
prices = np.array([[9,13.2], 
               [11.7,12.3], 
               [10.1,14.7] ,
               [11.8,14.9], 
               [13.2,13.1], 
               [6.9,9.6], 
               [12.1,10.6], 
               [12,13], 
               [11.7,9.1], 
               [9.84,11.89]])
amounts = np.array([[203674,18894], 
               [180785,54894], 
               [127802,18563] ,
               [28604,21963], 
               [600,900], 
               [38071,3555], 
               [35660,9005], 
               [15000,12000], 
               [48770,14370], 
               [6100,8980]])

total_amounts=amounts.sum(axis=0)
print("商品A最高成交價"+str(prices[0].max(axis=0)))
print("商品B最低成交量"+str(amounts[1].min(axis=0)))
print("商品A總成交量"+str(total_amounts[0])+"    商品B總成交量"+str(total_amounts[1]))
total_sales=(amounts*prices).sum(axis=0)
print("商品A總成交金額"+str(total_sales[0])+"    商品B總成交金額"+str(total_sales[1]))
print("商品A總均價"+str(total_sales[0]/total_amounts[0])+"    商品B總均價"+str(total_sales[1]/total_amounts[1]))
