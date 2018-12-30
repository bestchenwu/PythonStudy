# 继承Singleton的类在不重写__new__方法的前提下，都将会是单例类
# class Singleton(object):
#
#     # __new__相当于搭建框架,只有当__new__返回的值不是None,才可以继续执行init函数进行初始化
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls._instance
#
#
# s1 = Singleton()
# s2 = Singleton()
# print(s1 is s2)


class Singleton(type):

    def __init__(cls, *args, **kwargs):
        cls._instance = None
        super(Singleton, cls).__init__(*args, **kwargs)

    # 定义了call的方法的类，可以当作函数来使用，类似与abs等
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            # super函数接受两个参数 类的类型和实例对象
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=Singleton):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)
