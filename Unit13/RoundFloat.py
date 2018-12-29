class RoundFloat(float):
    # 所有的new方法都是类方法,通常用于从标准类中派生新方法
    def __new__(cls, val):
        return super(RoundFloat, cls).__new__(cls, round(val, 2))


val1 = RoundFloat(3.532)
print(val1)
