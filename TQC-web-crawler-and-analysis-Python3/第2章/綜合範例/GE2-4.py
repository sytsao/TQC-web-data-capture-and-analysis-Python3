# -*- coding: UTF-8 -*-

import csv
htmlname="file:PYA202input.html"
from urllib.request import urlopen
from bs4 import BeautifulSoup
file_name = "PYA202output.csv"
f = open(file_name, "w", encoding = 'utf8')
w = csv.writer(f)

html = urlopen(htmlname)
bsObj = BeautifulSoup(html, "lxml")

cell=bsObj.find("table").find("thead").find("tr").findAll("th")
F0 = cell[0].text
F1 = cell[1].text
F2 = cell[2].text
F3 = cell[3].text
F4 = cell[4].text
F5 = cell[5].text
data = [[F0,F1,F2,F3,F4,F5]]
w.writerows(data)
f.close()
