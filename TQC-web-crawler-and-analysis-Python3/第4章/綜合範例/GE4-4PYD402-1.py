# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
samples_1 = np.random.normal(loc=1, scale=.5, size=1000)
samples_2 = np.random.standard_t(df=10, size=1000)
bins = np.linspace(-3, 3, 50)
plt.subplot(2, 2, 1)
plt.hist(samples_1, bins=bins, alpha=0.5, label='samples 1')
plt.legend(loc='upper left');
plt.subplot(1, 2, 2)
plt.scatter(samples_1, samples_2, alpha=0.1);
plt.show()

