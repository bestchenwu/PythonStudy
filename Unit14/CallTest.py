class C(object):

    # 只有定义了__call__方法的类,其实例才可以当作函数一样调用
    def __call__(self, *args, **kwargs):
        print("I am called")


c = C()
c()
