def f(x, p):
    if x == 1:
        return True
    if x < 1 or p == 0:
        return False

    if x % 2 == 0:
        return f(x - 3, p - 1) + f(x - 2, p - 1) + f(x // 2, p - 1)

    return f(x - 2, p - 1) + f(x - 3, p - 1)
k = 0
for i in range(10, 51):
    if f(i, 5):
        k += 1
print(k)