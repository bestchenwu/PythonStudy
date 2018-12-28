def factories(n):
    if n <= 1:
        return 1
    else:
        return n * factories(n - 1)


print(factories(5))


# 尾递归优化
def factories1(n, base=1):
    if n <= 1:
        return base
    else:
        return factories1(n - 1, n * base)


print(factories1(5))
