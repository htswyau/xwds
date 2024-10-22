n = int(input())
def f(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = (1, 1)
    t = a + b
    for i in range(2, n-1):
        a, b = b, a + b
        t += b
    return t
r = f(n)
print(r)
