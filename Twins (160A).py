n = input()
x = input().split()
for i in range(len(x)):
    x[i] = int(x[i])
total,a,b,c = 0, 0, 0, 0
for i in x:
    total += i
x = sorted(x,reverse=True)
while 2*b <= total:
    b += x[c]
    c += 1
print(c)