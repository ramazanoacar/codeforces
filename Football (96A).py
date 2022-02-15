x = input()
zero = x.split('0')
one = x.split('1')
a = 0
for i in zero:
    if len(i) > 6:
        a = 1
        break
if a != 1:
    for j in one:
        if len(j) > 6:
            a = 1
            break
if a == 1:
    print('YES')
else:
    print('NO')