def f(x, y):
    if x > y or y == 135:
        return 0
    if x == y:
        return 1
    if y % 5 == 0 and y % 3 != 0:
        return f(x, y // 5) + f(x, y - 1)
    if y % 5 != 0 and y % 3 == 0:
        return f(x, y // 3) + f(x, y - 1)
    if y % 5 == 0 and y % 3 == 0:
        return f(x, y // 3) + f(x, y - 1) + f(x, y // 5)
    return f(x, y - 1)
print(f(2, 53) * f(53, 531))
