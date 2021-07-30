# python的地板除和真正的除法

# a = 1
# b = 2
# # 真正的除法 输出0.5
# print(a / b)
# # 地板除 输出0
# print(a // b)
#
# # 接受单值字符,输出ASCII整型数字
# c = ord('a')
# # 接受整型数字,输出ASCII的字符
# d = chr(97)
# print(c)
# print(d)
#
# # bool函数 对于值为0或者空列表 空map的情况,结果都为false,其他情况则为true
# e = bool(0)
# # 十六进制
# f = 0x32
# # 输出3*16+2 = 50
# print(f)
# # 八进制
# f = 0o14
# # 输出1*8+4 = 12
# print(f)

import random

n = 10
list = []
for i in range(1, n):
    list.append(random.randint(1, n))

print(list)
size = len(list)
print(list[random.randint(0, size)])
print(list[random.randint(0, size)])
print(list[random.randint(0, size)])
