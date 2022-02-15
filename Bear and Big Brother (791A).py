x = input().split()
a,b = int(x[0]), int(x[1])
c = 0
while a <= b:
    a = a*3
    b = b*2
    c += 1
print(c)