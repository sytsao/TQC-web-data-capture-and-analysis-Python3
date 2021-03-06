# -*- coding: utf-8 -*-
"""
集保戶股權分散表中0050的資料，主要欄位：資料日期、證券代號、持股分級、人數、股數、佔集保庫存數比例%
持股分級的定義，說明如下：
1.第1級至第15級，係持股為1:1-999 、2:1,000-5,000、3:5,001-10,000、4:10,001-15,000、
5:15,001-20,000、6:20,001-30,000、7:30,001-40,000、8:40,001-50,000、
9:50,001-100,000、10:100,001-200,000、11:200,001-400,000、12:400,001-600,000、
13:600,001-800,000、14:800,001-1,000,000、15:1,000,001以上等15個級距。
2.另考量交易市場偶因資料日前1營業日客戶帳戶賣出餘額不足之情事發生，
使各「持股分級」合計股數與發行公司已發行股份總數產生之差異，爰新增第16欄差異數調整。
3.第17欄為合計欄。
"""

import numpy as np
df1 = np.genfromtxt('集保戶股權分散表0050.csv', delimiter=',',encoding = 'utf8')
print("0050股東集保戶總人數"+str(df1[:,3].sum(axis=0)))
print("0050股東集保戶總股數"+str(df1[:,4].sum(axis=0)))
print("0050股東集保戶分級最低持有總股數"+str(df1[:,4].min(axis=0)))

