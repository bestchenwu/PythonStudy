class P(object):

    def foo(self):
        print("I am P foo")


class C(P):
    #bar = 'bar'

    def foo(self):
        # super用于寻找父类
        # super().foo()
        # dir后不带参数表示获取调用者的局部变量
        # 等价于locals().keys()
        print(dir())
        print("I am C foo")


c = C()
c.bar = 'jack'
# c.foo()
# 获取c的属性，与dir(c)类似,如果没有带参数，则等同于locals()
print(vars(c))
