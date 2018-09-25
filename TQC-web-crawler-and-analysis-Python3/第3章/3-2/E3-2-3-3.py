# -*- coding: utf-8 -*-
import numpy as np
data = [(2,'c',85.4),(3,'java',90),(4,'php',88)]
arr2 = np.array(data,dtype =[('no',int),('name','S10'),('score',float)])
print(np.sort(arr2,order='score'))
print(np.sort(arr2,order = ['no','score']))#多列组合排序
