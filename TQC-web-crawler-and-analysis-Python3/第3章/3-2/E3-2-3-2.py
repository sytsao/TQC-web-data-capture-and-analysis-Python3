# -*- coding: utf-8 -*-
import numpy as np
arr = np.array([[ 3,  2],[ 1,  6],[ 12,  11],[ 10,  9],[ 4, 8],[ 5, 7]])
print(arr)
print(arr.shape)
print(np.sort(arr))
print(np.sort(arr,axis=-1))
print(np.sort(arr,axis=0))
arr1=arr.reshape(3,2,2)
print(np.sort(arr1,axis=0))
print(np.sort(arr1,axis=1))
print(np.sort(arr1,axis=-1))

