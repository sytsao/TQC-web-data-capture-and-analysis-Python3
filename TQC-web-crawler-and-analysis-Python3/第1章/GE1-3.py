"""
上網路抓取開放資料進行處理-台北市Youbike
主要欄位：sno：站點代號、 sna：場站名稱(中文)、 tot：場站總停車格、 sbi：場站目前車輛數量、 
sarea：場站區域(中文)、 mday：資料更新時間、 lat：緯度、 lng：經度、 ar：地址(中文)、 
sareaen：場站區域(英文)、 snaen：場站名稱(英文)、 aren：地址(英文)、 bemp：空位數量、 
act：全站禁用狀態
"""

import urllib
import gzip
import json
import urllib.request
url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.gz'
with urllib.request.urlopen(url) as response:
    with gzip.GzipFile(fileobj=response) as f:
        jdata = f.read()
        f.close()
        data = json.loads(jdata)
fout=open('GE1-3-output.txt', 'w', encoding = 'utf8') 
for key,value in data["retVal"].items():
    sno = value["sno"]
    sna = value["sna"]
    mday = value["mday"]
    sbi = value["sbi"]
    print( "NO." + sno + " " + sna + " " +mday + " " + sbi)
    data="NO." + sno + " " + sna + " " +mday + " " + sbi
    fout.write(str(data)+'\n')
fout.close()