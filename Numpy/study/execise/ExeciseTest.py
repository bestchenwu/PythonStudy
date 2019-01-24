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
# 计算sepallength的softmax分数。
# def softMax(x):
#     ex = np.exp(x-np.max(x))
#     return ex/ex.sum(axis=0)
# print(softMax(array)[:4])
# 创建以下模式而不使用硬编码。只使用numpy函数和下面的输入数组a。
# a = np.array([1, 2, 3])
# # > array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
# b = np.repeat(a, repeats=3)
# c = np.tile(a, 3)
# d = np.concatenate((b, c))
# print(d)
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
# 期望array([2, 4])
# c=np.intersect1d(a,b)
# print(c)
# 从数组a中删除数组b中的所有项。
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])
# 期望输出array([1,2,3,4])
# c=np.setdiff1d(a,b)
# print(c)
# 获取a和b元素匹配的位置
# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# # 期望输出(array([1, 3, 5, 7]),)
# print(np.where(a==b))
# 获取5到10之间的所有项目。
# a = np.array([2, 6, 1, 9, 10, 3, 27])
# # 期望 (array([6, 9, 10]),)
# # np.where后面始终跟一个条件表达式
# print(a[np.where((a > 5) & (a <= 10))])


# 转换适用于两个标量的函数maxx，以处理两个数组
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

# pair_max(a, b)
# # > array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])
# def max(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
#
# max_v = np.vectorize(max, otypes=[float])
# print(max_v(a, b))

# 在数组arr中交换列1和2。
# arr = np.arange(9).reshape(3, 3)
# print(arr)
# print(arr[:, (0, 2, 1)])
# 反转二维数组arr的行。
# print(arr[::-1,])
# 创建一个形状为5x3的二维数组，以包含5到10之间的随机十进制数。
arr = np.random.randint(low=5, high=10, size=(5, 3))
# print(arr)
# 只打印或显示numpy数组rand_arr的小数点后3位。
# arr = np.random.rand(3,5)
# print(arr)
# np.set_printoptions(precision=3)
# print(arr)
# 创建一种标准化形式的鸢尾属植物间隔长度，其值正好介于0和1之间，这样最小值为0，最大值为1。
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

# array = (sepallength - sepallength.min()) / (sepallength.max() - sepallength.min())
# print(array)
# 计算sepallength的softmax分数。 归一化,所有项的和为1
# soft 公式= e(x-max(x))/sum(e(x-max(x))
# def softmax(x):
#     ex = np.exp(x-np.max(x))
#     return ex / np.sum(ex)
#
#
# print(softmax(sepallength))
# 找到鸢尾属植物数据集的第5和第95百分位数
# array = np.percentile(sepallength, [5, 95])
# print(array)
# 在iris_2d数据集中的20个随机位置插入np.nan值
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris_2d = np.genfromtxt(url, delimiter=',', dtype='float')
# np.random.seed(100)
# 得出iris_2d的行数和列数
# shapeTuple=iris_2d.shape
# iris_2d[np.random.randint(shapeTuple[0],size=20),np.random.randint(shapeTuple[1],size=20)]=np.nan
# print(iris_2d[:10])
# 在iris_2d的sepallength中查找缺失值的数量和位置（第1列）
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
# iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
# print("nan count:", np.isnan(iris_2d[:, 0]).sum())
# print("nan location", np.where(np.isnan(iris_2d[:, 0])))
# 过滤具有petallength（第3列）> 1.5 和 sepallength（第1列）< 5.0 的iris_2d行
# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
# condition = (iris_2d[:,2]>1.5) & (iris_2d[:,0]<5.0)
# print(iris_2d[condition])
# 选择没有任何nan值的iris_2d行。
# condition = np.sum(np.isnan(iris_2d), axis=1) == 0
# print(iris_2d[condition][:5])
# 在iris_2d中找出SepalLength（第1列）和PetalLength（第3列）之间的相关性
# 我们一般采用相关系数来描述两组数据的相关性，而相关系数则是由协方差除以两个变量的标准差而得，
# 相关系数的取值会在 [-1, 1] 之间，-1 表示完全负相关，1 表示完全相关
# print(iris_2d[:, 0])
# print(np.corrcoef(iris_2d[:, 0], iris_2d[:, 2])[0,1])
# 找出iris_2d是否有任何缺失值。
# print(np.isnan(iris_2d).any())
# 在numpy数组中将所有出现的nan替换为0
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
# iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
# array = np.where(np.isnan(iris_2d))
# # 以下两种方式是等价的
# # iris_2d[np.isnan(iris_2d)] = 0
# iris_2d[array] = 0
# print(iris_2d[:4])
#
# print(np.unique(iris_2d))
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
# 将iris_2d的花瓣长度（第3列）加入以形成文本数组，这样如果花瓣长度为：
#
#     Less than 3 --> 'small'
#     3-5 --> 'medium'
#     '>=5 --> 'large'
# np_bins = np.digitize(iris[:,2].astype('float'),[0,3,5,10])
# np_map = {1:'small',2:'medium',3:'large',4:np.nan}
# newArray = [np_map[x] for x in np_bins]
# print(newArray)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')
# 代表第一到第五列
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
# 在iris_2d中为卷创建一个新列，其中volume是（pi x petallength x sepal_length ^ 2）/ 3
# sepallength = iris_2d[:,0].astype(float)
# petallength =iris_2d[:,2].astype(float)
# new_volumn = (np.pi*petallength * (sepallength**2) /3)
# new_volumn = new_volumn[:,np.newaxis] # 将一维矩阵转换为二维矩阵
# print(np.hstack((iris_2d,new_volumn))[:4])
# 第42节练习

np.random.seed(100)
a = np.random.randint(1,10, [5,3])
print(a)
b= np.apply_along_axis(np.min,arr=a,axis = 1)
print(b)
