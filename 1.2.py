def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if y % 4 == 0 and y % 9 != 0:
        return f(x, y // 4) + f(x, y - 1)
    if y % 4 != 0 and y % 9 == 0:
        return f(x, y // 9) + f(x, y - 1)
    if y % 4 == 0 and y % 9 == 0:
        return f(x, y // 4) + f(x, y - 1) + f(x, y // 9)
    return f(x, y - 1)
print(f(2, 149))