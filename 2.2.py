def f(x, y):
    if x < y or x == 53:
        return 0
    if x == y:
        return 1
    if x % 5 == 0 and x % 3 != 0:
        return f(x // 5, y) + f(x - 1, y)
    if x % 5 != 0 and x % 3 == 0:
        return f(x // 3, y) + f(x - 1, y)
    if x % 5 == 0 and x % 3 == 0:
        return f(x // 3, y) + f(x - 1, y) + f(x // 5, y)
    return f(x - 1, y)
print(f(135, 35) * f(35, 2))
