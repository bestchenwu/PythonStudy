import sys
import operator
"this is a python module"
debug = True


class Foo(object):
    'FOO clsss'
    pass


def test():
#在python3中使用print(xx)而非print xx
#print("run test")
    foo='abcde'
    print(foo[::-2])
    #python3中没有cmp函数，改为使用lt
    a,b=-4,12
    print(operator.lt(a,b))



if __name__=='__main__':
    test()



