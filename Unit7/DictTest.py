dict1 = {}
dict2 = {"name": "haha","id": 1}
# 直接用构造方法创建dict
fdict = dict((['x',1], ['y',2]))
print(fdict)
# 使用fromkeys创建dict,表示每个key都对应同一个元素
fdict1 = {}.fromkeys(['x', 'y'], [-1, -2])
# 返回{'x':[-1, -2],'y':[-1, -2]}
# print(fdict1)
# # 如果不指定value值，则默认key对应的值都是None
# fdict2 = {}.fromkeys(['x', 'y'])
# print(fdict2)
# for key in fdict1.keys():
#     print("key=%s,value=%s" % (key, fdict1[key]))
# # 从python2.4开始，不需要再使用dict.keys方法来循环key
# for key in fdict1:
#     print("key=%s,value=%s" % (key, fdict1[key]))
print('server' in fdict1)
# 删除元素
del fdict1['x']
#print(fdict1['x'])
fdict2 = {'host': 'earth','port': 80}
import operator
#print(operator.gt(fdict1,fdict2))
fdict3 = dict(x=1, y=2)
# print(fdict3)
# fdict4 = fdict3.copy()
# print(fdict4)
# print(id(fdict3) == id(fdict4))
# 更新，如果键重复，则覆盖,如果没有，则添加进去
fdict5 = {'x': 2, 'y': 2, 'z': 8}
fdict3.update(fdict5)
print(fdict3)
# setDefault表示如果该键不存在，则赋值一个新值，如果存在，则返回该键对应的值
a = fdict3.setdefault('a', 88)
print(a)
y = fdict3.setdefault('y', 88)
print(y)
items = fdict3.items()
print(items)
