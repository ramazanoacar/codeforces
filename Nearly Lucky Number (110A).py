y = input()
a,b = 0, 0
for i in range(len(y)):
    if y[i] == '4' or y[i] == '7':
        a += 1
a = str(a)
for i in range(len(a)):
    if a[i] != '4' and a[i] != '7':
        b = 1
if b == 1:
    print('NO')
else:
    print('YES')