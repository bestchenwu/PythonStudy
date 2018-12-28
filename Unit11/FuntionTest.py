def foo():
    print("this is foo function")


def netbar(net, bar):
    "this is netbar function"
    print("net=%s" % net)
    print("bar=%s" % bar)


# 可以不指定参数名称
netbar(1, 3)
# 也可以显式指定参数名称,参数顺序可以自由调整
netbar(bar=3, net=1)
