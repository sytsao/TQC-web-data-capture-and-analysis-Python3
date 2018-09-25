# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)

plt.title("My lovely sin function")
plt.xlabel('x-axes')
plt.ylabel('values')

plt.xlim(-6,6)
plt.ylim(-1.2,1.2)
plt.plot(x, y, lw=3, label='$\sin$')
plt.plot(x, np.cos(x), lw=3, label='$\cos$')
plt.legend()
plt.show()