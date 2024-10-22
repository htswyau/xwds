a = []
for i in range(1, 11):
    a.append(i)
b = []
for i in range(11, 21):
    b.append(i)
print("исходные: ", a, b)
c = a
a = b
b = c
print("преобразованные: ", a, b)