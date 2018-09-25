# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import csv
x = []
y = []
with open('input.csv','r',encoding = 'utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))
plt.plot(x,y, label='banana')
plt.xlabel('date')
plt.ylabel('NT$')
plt.ylim([15, 25])
plt.title('Market Average Price')
plt.legend()
plt.show()