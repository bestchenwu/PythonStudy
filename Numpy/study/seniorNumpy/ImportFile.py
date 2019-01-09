import numpy as np

# 将科学计数法关闭
np.set_printoptions(suppress=True)  # if set to false,then
# array = np.genfromtxt('https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv', delimiter=',',
#                       skip_header=1, filling_values=-999, dtype=float)
# print(array[0, :])  # 输出第一行
# array = np.genfromtxt('https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv', delimiter=',',
#                       skip_header=1, filling_values=-999, dtype='object')
# print(array[0, :])  # 输出第一行
# array = np.array([1,2,3,4])
# # numpy supports npy and npz格式的保存
# np.save('numpy.npy',array)
# # 从文件中反读出来
# array2 = np.load('numpy.npy')
# # 每个位置的元素都一一做对比
# print(np.equal(array,array2))
array1 = np.zeros((2, 2))
array2 = np.ones((2, 2))
#  将两个矩阵合并到一块,通过参数axis来表示是横向叠加 还是纵向叠加
# axis 是代表第几维,当为0的时候就表示对二维数组按列,当为1的时候表示对二维数组按行
# axis = None则flat之后再叠加到一块
# axis = 0  表示按列
array3 = np.concatenate((array1, array2), axis=0)
# 输出 [0 0 0 0 1 1 1 1 ]
print(array3)
# axis = 0
# 输出
# [ 0 0
#  0 0
#  1 1
#  1 1]
