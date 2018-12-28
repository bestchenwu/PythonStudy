from random import randint
# 在python3中需要从functools中引用reduce函数了
from functools import reduce

# isOdd = lambda x: x % 2
#
# allNums = []
# for i in range(5):
#     allNums.append(randint(1, 88))
#
# print(allNums)
# filterObject = filter(isOdd, allNums)
# for item in filterObject:
#     print(item)

print("the final result is :%d " % reduce(lambda x, y: x + y, range(5)))
