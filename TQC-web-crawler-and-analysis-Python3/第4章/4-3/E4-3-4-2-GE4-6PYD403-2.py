# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
samples_1 = np.random.normal(loc=1, scale=.5, size=1000)
samples_2 = np.random.standard_t(df=10, size=1000)
bins = np.linspace(-3, 3, 50)

plt.scatter(samples_1, samples_2, alpha=0.2);
plt.show()

