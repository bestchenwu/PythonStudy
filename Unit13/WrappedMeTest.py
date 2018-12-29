class WrappedMe(object):

    def __init__(self, data):
        self.__data = data

    def get(self):
        return self.__data

    def __repr__(self):
        return 'self.__data'

    def __str__(self):
        return str(self.__data)

    def __getattr__(self, attr):
        print("attr = %s" % attr)
        return getattr(self.__data, attr)


wrappedComplex = WrappedMe(3 + 4j)
# 调用str函数
print(wrappedComplex)
# 调用__getattr__函数
print(wrappedComplex.real)
