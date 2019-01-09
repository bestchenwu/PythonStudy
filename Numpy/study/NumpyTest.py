import os
import numpy as np

# array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
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
# array2 = array1.sum(axis=0)
# print(array2)
# array3 = np.zeros(5)
# print(array3)
# array4 = np.random.rand(5)
# print(array4)
# array5 = np.ones((2, 4))
# print(array5)
#array1 =
# [1,2
#  3,4]
# array1 = np.array([[1, 2], [3, 4]])
# # array2=
# # [5,6
# #   7,8]
# array2 = np.array([[5, 6], [7, 8]])
# # print sum
# print(array1+array2)
# print(array1-array2)
# print(array1/array2)
# # 需要注意矩阵直接用乘法代表元素逐项相乘
# # [[1*5] [2*6]
# #  [3*7] [4*8]]
# print(array1*array2)
# # 矩阵乘法运算的方式是用dot,公式为:
# # [[ 1*5+2*7,1*6+2*8]
# #  [5*3+4*7],3*6+4*8 ]
# print(array1.dot(array2))

d=np.linspace(0,2*np.pi,5)