import operator
# aList = [1, 2, 3]
# # bList=aList[1:2]
# # print(bList)
# # print(type(bList))
# aList[2]='aa'
# print(aList)
# #增加元素
# aList.append('bbb')
# print(aList)
# #删除元素(根据索引下标删除)
# del aList[2]
# print(aList)
# #删除元素(根据元素内容删除)
# aList.remove('bbb')
# print(aList)
# numList = [43, -1.23, -2, 6.15]
# bList = numList[2:-1]
# print(bList)
# flag = 41 in numList
# print(flag)
# aList = [1, 2, 3]
# bList = aList*2
# print(bList)
# cList = [i for i in range(8) if i % 2 == 0]
# print(cList)
# dList = [4, 5, 6]
# print(dList > aList)
# 在python3中使用operator的gt、lt来进行比较
# print(operator.gt(dList, aList))
# aList.append(4)
# print(operator.gt(dList, aList))
# 列表的比较是先逐一比较各个元素，再比较列表长度
# print(len(aList))
aList = ['Then', 'aone', 'BOX']
# print(sorted(aList))
# for item in reversed(aList):
#     print(item)
# 在list与tuple之间转换
aTuple = tuple(aList)
print(aTuple)
bList = list(aTuple)
print(bList)
# 等值判断是比较元素内容
print(aList == bList)
# is操作是比较对象id
print(aList is bList)
bList.insert(2, 'haha')
print(bList)
#默认弹出最后一个元素
bList.pop()
print(bList)
