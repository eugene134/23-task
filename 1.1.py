def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if y % 3 == 0 and y % 5 != 0:
        return f(x, y // 3) + f(x, y - 8)
    if y % 3 != 0 and y % 5 == 0:
        return f(x, y // 5) + f(x, y - 8)
    if y % 3 == 0 and y % 5 == 0:
        return f(x, y // 5) + f(x, y - 8) + f(x, y // 3)
    return f(x, y - 8)
print(f(2, 358))

