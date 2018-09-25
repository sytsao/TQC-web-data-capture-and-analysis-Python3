# -*- coding: utf-8 -*-
datas = [[9,203674,13.2,18894], [11.7,180785,12.3,54894], [10.1,127802,14.7,18563] , 
[11.8,28604,14.9,21963], [13.2,600,13.1,900], [6.9,38071,9.6,3555], 
[12.1,35660,10.6,9005], [12,15000,13,12000], [11.7,48770,9.1,14370], 
[9.84,6100,11.89,8980]]
indexs= ["三重市","台中市","台北一","台北二","台東市","板橋區","高雄市","嘉義市","鳳山區","豐原區"]
columns = ["西瓜價", "西瓜量", "香瓜價", "香瓜量"]
import pandas as pd
df = pd.DataFrame(datas, columns=columns,  index=indexs)

print('行標題為項目，列題標為交易市場')
print(df)
print()

df1=df.sort_values(by="西瓜價", ascending=False)
print('以西瓜價遞減排序')
print(df1['西瓜價'])
print()

print('最後三筆的西瓜/香瓜價雨量')
print(df1.tail(3))
print()

df.loc["台北一","西瓜價"]
print('台北一市場的行情')
print(df.loc["台北一",:])

indexs[0] = "三重區"
df.index = indexs
columns[2] = "洋香瓜價"
columns[3] = "洋香瓜量"
print()
print('全體市場行情')
df.columns = columns
print(df)