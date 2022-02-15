x = []
a, b, c, d, e = 0, 0, 0, 0, 0
for i in range(5):
    x.append(input().split())
for i in x:
    a = 0
    for j in i:
        if '1' in j:
            c = 1
            break
        a += 1
    if c == 1:
        break
    b += 1
if a < 2:
    d = 2-a
else:
    d = a-2
if b < 2:
    e = 2-b
else:
    e = b-2
print(d+e)

