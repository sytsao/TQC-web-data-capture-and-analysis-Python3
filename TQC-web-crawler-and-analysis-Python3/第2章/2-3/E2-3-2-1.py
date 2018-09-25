# -*- coding: utf-8 -*-
'''
資料庫的讀寫使用 SQLAlchemy，透過sqlalchemy模組中的create_engine函數來建立sqlite的連線,
並設定將資料表儲存在memory中
'''
import json
import requests
import pandas as pd
from sqlalchemy import create_engine
req = requests.get('http://opendata2.epa.gov.tw/AQI.json')
data = json.loads(req.content.decode('utf8'))
df = pd.DataFrame(data)
engine = create_engine('sqlite:///:memory:')
df.to_sql('AQI_table', engine, index=False)
print(pd.read_sql_query('SELECT `County` as `縣市`, `SiteName` as `區域`, \
    CAST(`PM2.5_AVG` AS int) as `PM2.5` FROM `AQI_table` \
    order by CAST(`PM2.5_AVG` AS int) DESC', engine))