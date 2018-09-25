# -*- coding: utf-8 -*-
import requests
import json
url = 'http://opendata2.epa.gov.tw/AQI.json'
response = requests.get(url)
print('Content-Length:', response.headers['Content-Length'])
response = json.loads(response.text)
print('新北市PM2.5相關資料：')
for record in response:
    if record['County'] == '新北市':
        print('%s：' % record['SiteName'])
        print('\tAQI：%s' % record['AQI'])
        print('\tPM2.5：%s' % record['PM2.5'])
        print('\tPM10：%s' % record['PM10'])
        print('\t資料更新時間：%s' % record['PublishTime'])
