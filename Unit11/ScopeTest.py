x = 10


def foo():
    def bar():
        lambdaBar = lambda: x + y
        y = 5
        return lambdaBar

    print(bar()())


foo()
