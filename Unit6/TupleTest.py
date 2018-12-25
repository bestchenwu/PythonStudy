# 创建一个单元素的元组方法
# aTuple=('xyz')
# # 这实际上创建的是一个字符串
# print(type(aTuple))
# aTuple=('xyz',)
# # 在元素后面加一个逗号才是真元组对象
# print(type(aTuple))
import copy
person = ['name', ['save', 100]]
wifi = person
hubby = copy.deepcopy(person)
wifi[0] = 'marry'
hubby[0] = 'jack'
print(hubby, wifi)
wifiIdList = [id(i) for i in wifi]
hubbyIdList = [id(i) for i in hubby]
print(wifiIdList)
print(hubbyIdList)
