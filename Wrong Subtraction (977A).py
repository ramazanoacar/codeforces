x = list(input().split())
n, k = list(x[0]), int(x[1])
for i in range(k):
    if int(n[-1]) == 0:
        n.pop(-1)
    else:
        n[-1] = str(int(n[-1]) - 1)
s = ''.join(n)
print(s)