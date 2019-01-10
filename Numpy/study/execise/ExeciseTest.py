import numpy as np

# 将numpy导入为 np 并打印版本号
# print(np.__version__)
# # 如何创建一维数组？
# print(np.array([1, 2, 3, 4]))
# # 行向量转列向量
# print(np.transpose(np.array([[1, 2, 3, 4]])))
# #  如何创建一个布尔数组？
# print(np.full(shape=(2, 3), fill_value=True, dtype=bool))
# # 问题：从 arr 中提取所有的奇数
# array1 = np.random.randint(10, size=(2, 3))
# print(array1)
# index = np.where(array1 % 2 == 1)
# print(array1[index])
# # 如何用numpy数组中的另一个值替换满足条件的元素项？
# array1[array1 % 2 == 1] = -1
# # 将arr中的所有奇数替换为-1，而不改变arr。
# out = np.where(array1 % 2 == 1, -1, array1)
# print(out)
# 垂直堆叠数组a和数组b
a = np.random.randint(10, size=(2, 3))
# print(a)
b = np.random.randint(10, size=(2, 3))
# print(b)
# c = np.concatenate((a,b),axis=0)
# print(c)
# 获取数组a和数组b之间的公共项。
c = np.intersect1d(a, b)
# print(c)
# 从数组a中删除数组b中的所有项。
d = np.setdiff1d(a, b)

# print(d)
# setdiff1d
# print(np.where(a==b))
# 转换适用于两个标量的函数maxx，以处理两个数组。
# def max(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
#
# vectoryMax = np.vectorize(pyfunc=max)
# print(vectoryMax(a, b))
# 在数组arr中交换列1和2。
# print(a[:, (1, 0, 2)])
# # 交换数组arr中的第1和第2行：
# print(a[(1, 0), :])
# 反转二维数组arr的行。
# print(a[::-1,:])
# 创建一个形状为5x3的二维数组，以包含5到10之间的随机十进制数。
array = np.random.randint(low=5, high=10, size=(5, 3))
# print(array)
# 只打印或显示numpy数组rand_arr的小数点后3位。
# np.set_printoptions(precision=3)
np.random.seed(100)
# print(1e3) #  输出1000
array = np.random.rand(5) / 1e3
# print(array[:2,])
# 通过e式科学记数法来打印rand_arr（如1e10）
# np.set_printoptions(suppress=False)


# 将numpy数组a中打印的项数限制为最多6个元素。
# np.set_printoptions(threshold=6)
# array = np.arange(15)
# print(array)
# 打印完整的numpy数组a而不截断。
# 从前面问题中导入的一维鸢尾属植物数据集中提取文本列的物种。
# array = np.genfromtxt('https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv', delimiter=',',
#                       skip_header=1, dtype='object')
# print(array[:,-1])
# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
# 通过省略鸢尾属植物数据集种类的文本字段，将一维鸢尾属植物数据集转换为二维数组iris_2d。
array = np.genfromtxt('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', delimiter=',',
                      skip_header=1, filling_values=0, dtype='float', usecols=0)
# print(array.shape)
np.set_printoptions(suppress=True)
# 求出鸢尾属植物萼片长度的平均值、中位数和标准差(第1列)
# print(np.mean(array, axis=0))
# print(np.median(array, axis=0))
# print(np.std(array, axis=0))
# 创建一种标准化形式的鸢尾属植物间隔长度，其值正好介于0和1之间，这样最小值为0，最大值为1。
# s = array - array.min() / array.max() - array.min()
# print(s[:4])
#计算sepallength的softmax分数。
def softMax(x):
    ex = np.exp(x-np.max(x))
    return ex/ex.sum(axis=0)
print(softMax(array)[:4])
