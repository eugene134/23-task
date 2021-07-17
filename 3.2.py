count1 = 0
count2 = 0
def a(x, y, p):
    global count1
    if x > y:
        return 0
    if p == 7 and (x == y):
        count1 += 1
    else:
        a(x * 2, y, p + 1)
        a(x + 3, y, p + 1)
        a(x * 3, y, p + 1)
def b(x, y, k):
    global count2
    if x > y:
        return 0
    if k == 2 and (x == y):
        count2 += 1
    else:
        b(x * 2, y, k + 1)
        b(x + 3, y, k + 1)
        b(x * 3, y, k + 1)
a(2, 100, 0)
b(100, 900, 0)
print(count2 * count1)
