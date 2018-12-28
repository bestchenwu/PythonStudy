# @deco1(deco_arg)
# @deco2
# def func():
#     pass
from time import ctime, sleep


# 定义函数装饰器
def tsfunc(func):
    def wrappedfunction():
        print("time:%s funcName:%s is called" % (ctime(), func.__name__))
        return func()

    return wrappedfunction


@tsfunc
def foo():
    pass


# 实际这里相当定义tsfunc(args)(foo)
foo()


def convert(func, seq):
    "convert each elements in seq"
    return [func(item) for item in seq]


seq = ["2", "38", "-8"]
list1 = convert(int, seq)
print(list1)


def taxme(cost, rage=0.5):
    return cost * rage


print(taxme(100))
print(taxme(100, 0.1))


# 一个*表示是可变参数列表,两个**表示是可变参数字典
def tupleArgs(arg1, arg2="defaultArg2", *arg3, **arg4):
    print("arg1=%s arg2=%s " % (arg1, arg2))
    for item in arg3:
        print("arg3 item=%s" % item)
    for key in arg4:
        print("key=%s value=%s" % (key, arg4[key]))


tupleArgs(18, "arg2", "haha", "sweet")
tupleArgs(18, "arg2", "haha", "sweet", jack='1', marry='2')
