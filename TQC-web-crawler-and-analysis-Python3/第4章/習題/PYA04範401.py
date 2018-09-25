# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
data1=[1,4,9,16,25,36,49,64]
data2=[1,2,3,6,9,15,24,39]

seq=[1,2,3,4,5,6,7,8]

plt.plot(seq, data1, 'b--.',seq, data2,'r--.', linewidth=1)
plt.axis([0,8,0,70])
plt.title("Figure", fontsize=24)
plt.xlabel("x-Value", fontsize=16)
plt.ylabel("y-Value", fontsize=16)

plt.show()

