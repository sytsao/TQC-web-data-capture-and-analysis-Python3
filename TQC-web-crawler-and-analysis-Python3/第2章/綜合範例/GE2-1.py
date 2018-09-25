# -*- coding: UTF-8 -*-

import csv
htmlname="file:GE2-1-input.html"
from urllib.request import urlopen
from bs4 import BeautifulSoup
file_name = "GE2-1-output.csv"
f = open(file_name, "w", encoding = 'utf8')
w = csv.writer(f)

html = urlopen(htmlname)
bsObj = BeautifulSoup(html, "lxml")

for single_tr in bsObj.find("table").find("tbody").findAll("tr"):
    cell = single_tr.findAll("td")
    F0 = cell[0].text
    F1 = cell[1].text
    data = [[F0,F1]]
    w.writerows(data)
f.close()
