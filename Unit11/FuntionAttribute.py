def foo():
    "this is foo function"
    pass

    def bar():
        print("bar doc:"+bar.__doc__)
        pass

    bar.__doc__ = "this is bar function in bar"
    bar()


foo()
