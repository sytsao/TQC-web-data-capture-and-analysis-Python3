# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import csv
a = []
b = []
with open('集保戶股權分散表.csv','r',encoding = 'utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if row[1]=='0050' and int(row[2])<16:
            a.append(row[2])
            b.append(float(row[5]))
plt.bar(a,b,label='0050')
plt.xlabel('category')
plt.ylabel('%')
plt.ylim(0,100)
plt.title('Settlement shareholding table')
plt.legend()
plt.show()
