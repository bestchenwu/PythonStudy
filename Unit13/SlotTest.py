class SlottedClass(object):
    '定义只允许类实例可以包含的属性'
    __slots__ = 'foo'
    pass


slotted = SlottedClass()

slotted.foo = 3
# 由于bar不在__slots__定义里，所以会报错误
# AttributeError: 'SlottedClass' object has no attribute 'bar'
slotted.bar = 5
