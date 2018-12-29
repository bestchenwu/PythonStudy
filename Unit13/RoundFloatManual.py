class RoundFloatManual(object):

    def __init__(self, value):
        assert isinstance(value, float), "value must be float"
        self.value = round(value, 2)

    # 相当于覆盖了toString()方法，在调用str(object)方法的时候会调用object的__str__方法
    def __str__(self):
        return "%.2f" % self.value


manual = RoundFloatManual(43.8821)
print(manual)
