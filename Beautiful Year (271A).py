n = int(input())
a,b = n, 0
while b == 0:
    a += 1
    d = str(a)
    c = 0
    for i in range(3):
        if d[i] in d[i+1:]:
            c = 1
    if c == 0:
        break
print(a)

