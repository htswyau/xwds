def ost(a, b):
    if a < b:
        return a
    else:
        return ost(a - b, b)
print(ost(100, 7))