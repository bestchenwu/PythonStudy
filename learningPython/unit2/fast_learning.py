# 本章描述python的快速入门
import decimal


# print("%s is number %d" % ("python", 1))
# 在python2中使用的是raw_input
# num = input("please enter your num:")
# print("double your %d is %d" % (int(num), (int(num) * 2)))
#
#
# def foo():
#     """this is a foo function"""
#     pass
#
#
# a = decimal.Decimal('1.1')
# print(a)

# python = 'python'
# # 默认print都会换一行
# print(python[3:], end='')
# print(python[2:4])
# print(python * 2)
#
# tuple = ('python', 1, 5.5, 'haha')
# print(tuple[2:])
# print(tuple[2])
# adict = {'post': 'earth'}
# adict['haha'] = 'sweet'
# adict['jack'] = 11
# print(adict)

# count = 0
# while count < 3:
#     print("coun=%d" % count)
#     count += 1

# foo = 'hello raoshanshan'
# # for i in range(len(foo)):
# #     print(foo[i], 'index=%d' % i)
# # 第一个是索引下标,第二个是字符
# for index, ch in enumerate(foo):
#     print(ch, 'index=%d' % int(index))

# 寻找0-4的奇数的平方
# list = [x ** 2 for x in range(5) if not x % 2 == 0]
# print(list)

# file = open('D:/logs/flink.properties', 'r')
# for line in file:
#     print(line,end='')
# file.close()

# index = 0
# while index <= 10:
#     print("index=%d" % index)
#     index += 1

# for index in range(1, 11, 1):
#     print("index=%d" % index)

# tuple = (1, 5, 9.2, 8.75, 23.4)
# sum = 0
# for i in tuple:
#     sum += i
# print("average is %f" % (float(sum) / len(tuple)))

# while True:
#     num = input("please input num from 0 to 100:")
#     if int(num) > 0 and int(num) < 100:
#         break


def sort(x, y, z):
    if x > z:
        tmp = x
        x = z
        z = tmp
    if y > z:
        tmp = y
        y = z
        z = tmp
    if x > y:
        tmp = x
        x = y
        y = tmp
    print("x,y,z:", x, y, z)


sort(1, 15, 7)
