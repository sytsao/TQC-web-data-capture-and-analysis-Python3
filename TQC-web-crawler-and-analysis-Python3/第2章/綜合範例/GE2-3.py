# -*- coding: UTF-8 -*-
#抓取生活資訊網中信義房屋分店資訊
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
file_name = "GE2-3-output" + ".csv"
f = open(file_name, "w", encoding = 'utf8')
w = csv.writer(f)
httphead="http://www.319papago.idv.tw/lifeinfo/sinyi/sinyi-"
for i in range(1,23):
    if i<10:
        htmlname=httphead+"0"+str(i)+".html"
    else:
        htmlname=httphead+str(i)+".html"
    html = urlopen(htmlname)
    bsObj = BeautifulSoup(html, "lxml")
    count=0
    for single_tr in bsObj.find("table", {"width":"728","border":"1" }).findAll("tr"):
        cell = single_tr.findAll("td")
        name = cell[0].contents[0]
        tel = cell[1].contents[0]
        address = cell[2].contents[0]
        print(name,tel, address)
        data = [[name,c tel, address]]
        if i>1 and count>0:
            w.writerows(data)
        count=count+1
f.close()
