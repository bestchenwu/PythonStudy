class DevNull(object):

    # 当进行对象获取调用
    def __get__(self, instance, owner):
        print('instance=%s' % instance)
        pass

    # 当进行对象设值时候调用
    def __set__(self, instance, value):
        print('value=%s' % value)
        pass

class C1(object):
    # 定义一个类属性
    foo = DevNull()

c1 = C1()
c1.foo = '123'
# 返回NONE
print(c1.foo)
