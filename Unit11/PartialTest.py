from operator import add, mul
from functools import partial

# 这里等同于add(x,11)
add11 = partial(add, 11)
print(add11(55))

secondInt = partial(int, base=2)
print(secondInt('10010'))
