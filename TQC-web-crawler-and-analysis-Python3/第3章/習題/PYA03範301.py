# -*- coding: utf-8 -*-
import pandas as pd
datas = [[75,62,85,73,60], [91,53,56,63,65], [71,88,51,69,87],[69,53,87,74,70] ]

indexs = ["小林", "小黃", "小陳", "小美"]
columns = ["國語", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)

print('行標題為科目，列題標為個人的所有學生成績')
print(df)
print()


print('後二位的成績')
print(df.tail(2))
print()


df1=df.sort_values(by="自然", ascending=False)
print('以自然遞減排序')
print(df1['自然'])
print()


df.loc["小黃","英文"]=80
print('小黃的成績')
print(df.loc["小黃",:])




indexs[0] = "小張"
df.index = indexs
columns[3] = "理化"
print()
print('全體成績')
df.columns = columns
print(df)
df.plot()