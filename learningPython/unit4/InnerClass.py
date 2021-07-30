import operator


# python3 以后就没有cmp函数了，改为使用operator模块的函数

# a, b = -4, 12
#
# flag = operator.lt(a, b)
# print(flag)
#
# str0 = str(4.3 - 2.1j)
# print("str0="+str0)

def displayNumType(num):
    print(num, ' is ', end=' ')
    # python3 取消了long,长整型和int合并,double类型也和float合并
    if isinstance(num, (int, float, complex)):
        print(type(num).__name__)
    else:
        print('not a number')


x = "abc"
displayNumType(x)

y = "cde"
print(type(x) == type(y))
print(type(x) is type(y))
