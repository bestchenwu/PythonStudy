class ObjectCreater(object):
    pass


#
# def echo(o):
#     print(o)
#
#
# # python中的类也是对象
# echo(ObjectCreater)
# echo(hasattr(ObjectCreater, 'new_attribute'))
#
# ObjectCreater.new_attribute = 'test'
# echo(hasattr(ObjectCreater, 'new_attribute'))
# type函数接受3个参数,分别为class名称、父类元组、类属性组成的字典
# myClass = type('ObjectCreater', (), {'bar': True})
# print(myClass)
# myObject = myClass()
# print(myObject.bar)

# 自定义元类,仿照type函数，接受三个参数，以此为当前类名，当前类的父类元组，当前类的属性字典
def upper_attr(future_classname, future_class_parents, future_attrs):
    # 选择所有不以__开头的属性
    # 对字典调用items()方法是获取所有内容的键值对元组的列表
    attrs = ((key, value) for key, value in future_attrs.items() if not key.startswith('__'))
    upper_attrs = dict((key.upper(), value) for key, value in attrs)
    return type(future_classname, future_class_parents, upper_attrs)


# python3中重写metaclass的方式
class UpperObject(metaclass=upper_attr):
    # python2的表达方式
    # __metaclass__ = upper_attr
    bar = 'test'


# upperObject = UpperObject()
print(hasattr(UpperObject, 'bar'))


def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass

        return Foo
    else:
        class Bar(object):
            pass

        return Bar

# myClass = choose_class('bar')
# print(myClass)
# print(myClass())
