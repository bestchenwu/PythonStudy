# object是所有类的父类,如果没有指定父类的时候，则默认为object
class MyObject(object):
    'first object sample'

    def __init__(self, nm, bb):
        self.nm = nm
        self.bb = bb
        print('you invoke init function')

    def printObject(self):
        print("nm=%s bb=%s" % (self.nm, self.bb))

    def updateNm(self, nm):
        self.nm = nm


class MyEmailObject(MyObject):
    'with email object'

    # 在类里面定义属性，相当与java里的静态属性
    foo = 'test'

    def __init__(self, nm, bb, email):
        MyObject.__init__(self, nm, bb)
        self.email = email

    def updateEmail(self, email):
        self.email = email

    # 这里的cls等价于self
    # staticmethod注解表示静态方法
    @staticmethod
    def postEmail(cls):
        print("post email :%s " % cls.email)


# myObject = MyObject('abc', '111')
# myObject.printObject()
# myObject.updateNm('haha')
# myObject.printObject()
#
# # myObject.x = 4
# # myObject.y = 5
# # print(myObject.x + myObject.y)
#
myEmailObject = MyEmailObject('abc', '111', '11@11.com')
# # myEmailObject.updateNm('jack')
# # myEmailObject.printObject()
# # print(dir(MyEmailObject))
# # print(MyEmailObject.__module__)
# print(type(myEmailObject))
# print(type(MyEmailObject))

MyEmailObject.postEmail(myEmailObject)
myEmailObject.postEmail(myEmailObject)

print(hasattr(myEmailObject,'foo'))
print(getattr(myEmailObject,'foo'))
delattr(myEmailObject,'foo')
print(hasattr(myEmailObject,'foo'))