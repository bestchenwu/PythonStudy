x = 3
y = 2
# python3的三元操作符号
z = x if x > y else y
print(z)

# count = 0
# while count < 9:
#     print("count=%d" % count)
#     count += 1
#
# for eachLetter in 'Names':
#     print("letter=%s" % eachLetter)

# 对于序列循环还可以使用索引
nameList=['sweet', 'haha', 'wuhan']
length = len(nameList)
for index in range(length):
    print("index=%d,name=%s" % (index,nameList[index]))
