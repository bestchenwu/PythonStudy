import numpy as np

# a =  [  2  1 -2
#         3  0  1
#         1  1  -1]
# b= [ -3
#       5
#       2]
# 求ax = b
a = np.array([[2, 1, -2], [3, 0, 1], [1, 1, -1]])
b = np.transpose(np.array([-3, 5, 2]))
x = np.linalg.solve(a, b)
print(x)
# 判断两个矩阵是否在允许的范围内相等
print(np.allclose(np.dot(a, x), b))
