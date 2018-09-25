# -*- coding: UTF-8 -*-
import csv
htmlname="https://www.cbc.gov.tw/lp.asp?CtNode=645&CtUnit=308&BaseDSD=32&mp=1"
from urllib.request import urlopen
from bs4 import BeautifulSoup
file_name = "GE2-6-output.csv"
f = open(file_name, "w", encoding = 'utf8')
w = csv.writer(f)

html = urlopen(htmlname)
bsObj = BeautifulSoup(html, "lxml")
count=0
for single_tr in bsObj.find("table",{"class":"DataTable2"}).findAll("tr"):
    if count==0:
        cell = single_tr.findAll("th")
    else:
        cell = single_tr.findAll("td")
    F0 = cell[0].text
    F1 = cell[1].text
    data = [[F0,F1]]
    w.writerows(data)
    count=count=1
f.close()
