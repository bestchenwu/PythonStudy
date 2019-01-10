import numpy as np

arr_x = np.random.randint(10, size=(3, 4))
print(arr_x)


def maxmin(x):
    return np.max(x) - np.min(x)


# apply_along_axis表示对矩阵,按列或者行 循环调用指定的func1d函数
print("the max row is ", np.apply_along_axis(func1d=maxmin, axis=0, arr=arr_x))
# 求一列或者一行中的最大值
print("the max row is ", np.apply_along_axis(func1d=np.max, axis=0, arr=arr_x))
