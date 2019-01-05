import os
import numpy as np
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(array1.shape)
# print(array1[1][2])
# # 1 means rows,:means columns
# y = array1[1,:]
# # [4 5 6]
# print(y)
# y = array1[:,1]
# # [2,5]
# print(y)
# y = array1[0:1,1]
# # [2]
# print(y)
# axis means
array2 = array1.sum(axis=0)
print(array2)
