import numpy as np

arr = np.random.randint(8, size=(3, 4))
print(arr)
# 对所有行/列排序的方式是:
# 表示按行进行排序
# arr2 = np.sort(arr, axis=1)
# print(arr2)
# 按列排序
# argsortIndex = np.argsort(arr, axis=0)
# 只按第一列进行排序,对其他列不产生影响
# argsortIndex = arr[:, 0].argsort()
# print(arr[argsortIndex])
# 对两列及两列以上的数组进行排序
# 要记住 先把要排序的列 最右边的放在第一个位置,其次放在第二个位置
array2 = np.lexsort((arr[:, 1], arr[:, 0]), axis=0)
print(arr[array2])
