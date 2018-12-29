class Time60(object):

    def __init__(self, minute, seconds):
        self.minute = minute
        self.seconds = seconds

    def __str__(self):
        return "%d:%d" % (self.minute, self.seconds)

    def __add__(self, other):
        if not isinstance(other, Time60):
            raise TypeError("other must be Time60")
        return Time60(self.minute + other.minute, self.seconds + other.seconds)

    # iadd 操作等同于自加运算 类似于m+=n
    def __iadd__(self, other):
        if not isinstance(other, Time60):
            raise TypeError("other must be Time60")
        self.minute += other.minute
        self.seconds += other.seconds
        return self


c1 = Time60(11, 22)
c2 = Time60(8, 13)
print("c1,c2=%s %s" % (c1, c2))
c3 = c1.__add__(c2)
print("c3 = %s" % c3)
c1.__iadd__(c2)
print("c1=%s" % c1)
