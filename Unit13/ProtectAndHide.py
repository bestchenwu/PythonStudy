class ProtectAndHide(object):
    def __init__(self, x):
        assert isinstance(x, int), "x must be integer"
        # 取相反数
        self.__x = ~x

    def get_x(self):
        return ~self.__x

    x = property(get_x)


# AssertionError: x must be integer
# protect = ProtectAndHide('foo')
protect1 = ProtectAndHide(35)
# AttributeError: can't set attribute
# 因为x被包装起来了，只允许get
# protect1.x = 32
print(protect1.x)
