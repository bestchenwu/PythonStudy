class P(object):

    def foo(self):
        print("I am P foo")


class C(P):

    def foo(self):
        # super用于寻找父类
        super().foo()
        print("I am C foo")


c = C()
c.foo()
