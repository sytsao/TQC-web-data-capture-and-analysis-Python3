# -*- coding: UTF-8 -*-
import requests
import json
#開放資料連結
url = 'http://data.ntpc.gov.tw/od/data/api/6DCFF24A-838C-40FB-A9DF-F1160AFAFE84?$format=json'
#發出HTTP GET請求
res = requests.get(url)
#將回傳結果轉換成標準JSON格式
data = json.loads(res.text)
#輸出新北市大專院校名單
print('新北市大專院校名單：\n')
for record in data:
    if record['type'] == '大專院校':
        print('名稱：%s' % record['name'])
        print('地址：%s' % record['address'])
        print('聯絡電話：%s' % record['tel'])
        print('網站：%s' % record['website'])
        print('資料更新時間：%s' % record['update_date'])
        print()

