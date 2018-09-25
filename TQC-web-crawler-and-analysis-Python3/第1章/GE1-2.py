"""
上網路抓取開放資料進行處理-農產品交易行情
主要欄位：交易日期、作物代號、作物名稱、市場代號、市場名稱、上價、中價、下價、平均價、交易量
"""
import urllib
import csv
import json
import urllib.request
url = 'http://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx'
with urllib.request.urlopen(url) as response:
    jdata = response.read()
    data1 = json.loads(jdata)
data=sorted(data1, key=lambda k: k["交易量"],reverse=True)

with open("GE1-2-output.csv", "w",encoding = 'utf8') as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['交易日期'], item['作物名稱'],item['市場名稱'], item['平均價'],item['交易量']])