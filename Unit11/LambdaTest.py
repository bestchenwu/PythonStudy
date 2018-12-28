# 测试lambda函数

# def add(x,y):return x+y ? lambda x,y:x+y
square = lambda x: x ** 2
print(square(3))

add = lambda x, y=2: x + y
print(add(3, 5))
print(add(8))
