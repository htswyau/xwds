a = input("текст: ")
def maxlen(a):
    m = 0
    c = 0
    for x in a:
        if x == 'н':
            c += 1
            m = max(m, c)
        else:
            c = 0
    return m
a = a.replace('!', '.')
print(maxlen(a))
print(a)