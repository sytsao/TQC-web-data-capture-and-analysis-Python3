#e6-3-7: 上網路抓取開放資料進行處理樣本資料做常態分配檢定
import pandas as pd
df1 = pd.read_csv('Dengue_Daily_last12m.csv',encoding="utf-8", sep=",",header=0)
#data=df1.describe()
df_county=df1.groupby("居住縣市").count()
print(df_county.sort_values("內政部居住鄉鎮代碼", ascending=False))
print(df1.groupby("是否境外移入").count())
df_country=df1.groupby("感染國家").count()
print(df_country.sort_values("內政部居住鄉鎮代碼", ascending=False).head(5))
df_taipei=df1[df1.居住縣市=="台北市"]
print(df_taipei.groupby("居住鄉鎮").count())
print(df_taipei.發病日.max())


