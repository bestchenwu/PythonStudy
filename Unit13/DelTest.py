class C(object):

    def __init__(self):
        print("init C object")
        # 构造函数不允许有返回值，返回值只能是None
        # return 1

    def __del__(self):
        print("del C object")
        # 析构函数允许有返回值，但是这个返回值没有多大实际意义
        # return 1

c1 = C()
# c3 = c1
# c2 = c1
# print(id(c1), id(c2), id(c3))
# del c1
# # 当所有的引用删除时候触发del析构函数
# del c2
# # del c3

# 实例属性
print(dir(c1))
print(c1.__dict__)
print(c1.__class__)

c1.foo = 'haha'

print(dir(c1))
print(c1.__dict__)
print(c1.__class__)