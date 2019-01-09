import numpy as np

# array1 = np.random.randint(5, size=[2, 3])
# print(array1)
# # axis 表示按行还是列排序
# # 0表示按列排序,1表示按行排序
# array1.sort(axis=1)
# print(array1)
array = np.random.randint(5, size=[4])
print(array)
indexArray = np.argsort(array)
# 排序后的索引数组
print(indexArray)
print(array[indexArray])