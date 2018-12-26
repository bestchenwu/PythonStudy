# 实际上是把字符串按照序列的方式 转换为set
# 集合类的元素不允许重复
set1 = set('hahat')
set2 = frozenset('hewa')
# print(set1)
# print(len(set1))
# # print(set2)
# # print(len(set2))
# # print('h' in set1)
# # for item in set1:
# #     print(item)
# set1.add(' wuhan')
# print(set1)
# # 不可变集合不可调用add方法
# print(set('posh') == set('opsh'))
# | 表示并集,& 表示交集,-表示差集
unionSet = set1 | set2
print(unionSet)

andSet = set1 & set2
print(andSet)
# 属于set1但不属于set2
differenceSet = set1-set2
print(differenceSet)
# 对称差分(即不属于set1也不属于set2)
symmetricDifferenceSet = set1 ^ set2
print(symmetricDifferenceSet)



