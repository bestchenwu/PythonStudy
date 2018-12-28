def foo():
    a = 123
    aString = "abc"
    print("foo()'s globals ", globals().keys())
    print("foo()'s locals", locals().keys())


foo()
print("outer's globals", globals().keys())
print("outer's locals", locals().keys())
