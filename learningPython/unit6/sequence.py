# python的序列格式的对象

list0 = [1, 2, 3, 4]
# print(list[1:2])
# print(list[-2:-5:-1])
# print(list * 2)
# print(list[2:])
# print(list[-2:])

# for i in range(-1, -len(list), -1):
#     print(list[:i])
rangeList = [i for i in range(-1, -len(list0), -1)]
for i in [None] + rangeList:
    print(list0[:i])

list1 = [5, 6, 7]
newList = list(zip(list0, list1))
# 输出每个位置组成的新元祖,然后再组成一个链表
print(newList)

url = """http://
      www.baidu.com
      jack"""
print(url.strip('\n'))
url = 'http://''www.baidu.com'
print(url)
url = 'hello world'+u'!'
print(url)
