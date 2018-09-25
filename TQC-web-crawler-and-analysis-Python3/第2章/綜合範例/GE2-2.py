# -*- coding: UTF-8 -*-

import csv
htmlname="file:GE2-2-input.html"
from urllib.request import urlopen
from bs4 import BeautifulSoup
file_name = "GE2-2-output.csv"
f = open(file_name, "w", encoding = 'utf8')
w = csv.writer(f)

html = urlopen(htmlname)
bsObj = BeautifulSoup(html, "lxml")

for single_tr in bsObj.find("table").find("tbody").findAll("tr"):
    cell = single_tr.findAll("td")
    F0 = cell[0].contents
    F1 = cell[1].contents
    F2 = cell[2].contents
    F3 = cell[3].contents
    data = [[F0,F1,F2,F3]]
    w.writerows(data)
f.close()
