a = []
l = int(input("длина массива: "))
for i in range(l):
    e = int(input())
    a.append(e)
print(min(a), sorted(a, reverse=True))