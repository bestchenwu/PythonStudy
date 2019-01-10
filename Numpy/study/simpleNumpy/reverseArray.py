import numpy as np

array = np.random.randint(10, size=(2, 3))
print(array)
# 只对行进行反转
# print(array[::-1, ])
# 对行和列全部反转
# print(array[::-1, ::-1])
# ravel和flattern的区别是前者实际上和原数组共享一片内存，当前者改变的时候也会影响原数组
print(array.ravel())
