import numpy as np

# 将从0到np.pi*2区间  等分为5个区间
# d = np.linspace(0,np.pi*2, 5)
# # [0.         1.57079633 3.14159265 4.71238898 6.28318531]
# print(d)
# 二维矩阵
# 1 2 3
# 4 5 6
# 7 8 9
# array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # 这是截取从0到第二行(不包括第二行) 的第二列
# print(array1[0:2, 2])  # 输出[3 6]
# print(array1[1, 1:])  # 输出[5 6]
# # 输出数组的属性
# print(array1.dtype) # 输出int32 (32表示是短整型)
# print(array1.itemsize) #一个短整型占4个字节

a = np.arange(0, 9)
# 把一维数组转换为3*3维数组
# a = a.reshape((3, 3))
# print(a)
# b = a
# print(a + b)
# print(a * b)
# print(np.dot(a, b))
# a = np.arange(0, 100, 10)
# print(a)
# indicies = [1, 5, -1]
# print(a[3])  # 输出30
# print(a[indicies]) # 相当于对数组a取三个索引值,分别为a[1],a[5],a[-1](取最后一个元素)
# a = np.arange(0, 50, 5)
# print(a)
# print(np.where(a > 30))  # 输出满足条件的数组下标
# 行向量和列向量的转换
# a = np.array([[1, 2, 3]])
# print(a)
# b = np.transpose(a)  # 将行列式转为列
# print(b)
# 创建两行两列的矩阵
# c = np.ones((2, 2))
# print(c)
# a = np.array([1, 2, 3])
# b = np.tile(a, 2)  # 单纯的把向量重复一遍
# c = np.repeat(a, 2)  # 对向量的每个元素重复一遍
# print(b)
# print(c)
rn = np.random.RandomState(100)
# rarray = rn.rand(2, 2)  # 在0,1之间取四个数组成二维数组
# print(rarray)
rarray1 = rn.randint(5, size=(2, 4))
print(rarray1)
# 计算出矩阵里不重复元素以及不重复的次数
# array, count = np.unique(rarray1, return_counts=True)
# print(array)
# print(count)
indexArray = np.where(rarray1 > 2)
print(indexArray)
# filterArray = rarray1[indexArray]
# print(filterArray)
filterArray = rarray1.take(indexArray)
print(filterArray)