# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
labels = 'Jun', 'Jul', 'Aug', 'Sep'
sizes = [20, 30, 40, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0, 0.1, 0) 
plt.subplot(1, 2, 1)
plt.bar(labels, sizes, color="blue") 
plt.subplot(1, 2, 2)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%')
plt.axis('equal')
plt.show()