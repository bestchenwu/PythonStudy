# def foo():
#     print("calling foo function")
#     global bar
#     bar = 200
#     print("after foo function called")
#     bar = 100
#     return bar
#
# print("bar=%d" % foo())
# print("bar is still = %d " % bar)


def foo1():
    m = 4

    def bar():
        n = 5
        lambdaBar = lambda: m + n
        return lambdaBar()

    print(bar())


foo1()
