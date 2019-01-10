import numpy as np


def foo(x):
    if x % 2 == 1:
        return x ** 2
    else:
        return x / 2


print("x = 10 ,foo:", foo(10))
print("x = 11 ,foo:", foo(11))

# 使得函数支持列表调用
foo_v = np.vectorize(foo, otypes=[float])
print(foo_v((10, 11, 12)))
