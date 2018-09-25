# -*- coding: UTF-8 -*-
#抓取新北勢房仲公會會員名冊
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
file_name = "新北市仲介" + ".csv"
f = open(file_name, "w", encoding = 'utf8')
w = csv.writer(f)
httphead="http://www.tcr.org.tw/a/table_blogs/index/21654"
for i in range(1,17):
    if i==1:
        htmlname=httphead
    else:
        htmlname=httphead+"?page="+str(i)
    html = urlopen(htmlname)
    bsObj = BeautifulSoup(html, "lxml")
    count=0
    for single_tr in bsObj.find("table").find("table").findAll("tr"):
        if count==0:
            cell = single_tr.findAll("th")
            F0 = cell[0].contents
            F1 = cell[1].contents
            F2 = cell[2].contents
            F3 = cell[3].contents
            F4 = cell[4].contents
        else:
            cell = single_tr.findAll("td")
#            print(cell)
            F0 = cell[0].a.string
            F1 = cell[1].a.string
            F2 = cell[2].a.string
            F3 = cell[3].a.string
            F4 = cell[4].a.string
        print(F0,F1,F2,F3,F4)
        data = [[F0,F1,F2,F3,F4]]
        if i>1 and count>0:
            w.writerows(data)
        count=count+1
f.close()
