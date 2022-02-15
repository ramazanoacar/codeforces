x,f = 0,0
n = int(input())
lst = input().split()
for i in lst:
    if int(i) > 0 :
        f += int(i)
    else:
        if f == 0:
            x += int(i)
        else:
            f += int(i)
print(-x)


