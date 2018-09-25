# -*- coding: UTF-8 -*-
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
file_name = " E2-2-2-2-output.csv"
f = open(file_name, "w", encoding = 'utf8')
w = csv.writer(f)
htmlname="file:E2-2-2-2-input.html"
html = urlopen(htmlname)
bsObj = BeautifulSoup(html, "lxml")
for single_tr in bsObj.find("table").find("tbody").findAll("tr"):
    cell = single_tr.findAll("td")
    F0 = cell[0].text
    F1 = cell[1].text
    data = [[F0,F1]]
    w.writerows(data)
f.close()
