x = list(input())
y = list(input())
for i in range(len(x)):
    if x[i] != y[-(1+i)]:
        print('NO')
        exit()
print('YES')