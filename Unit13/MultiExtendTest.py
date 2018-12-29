class P1(object):
    # class P1():
    def foo(self):
        print("P1 foo called")


class P2(object):
    # class P2():
    def foo(self):
        print("P2 foo called")

    def bar(self):
        print("P2 bar called")


class C1(P1):
    pass


class C2(P2):

    def bar(self):
        print("C2 bar called")


class GC(C1, C2):
    pass


gc = GC()
# 经典继承算法 深度优先遍历,从左往右,会使用P1.foo
gc.foo()
gc.bar()
print(isinstance(gc, C2))
