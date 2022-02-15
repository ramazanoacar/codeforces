x = int(input())
for i in range(x):
    a = input().split()
    n, k = int(a[0]), int(a[1])
    b,c = 0, 0
    lst = []
    for i in range(n):
        lst.append('.')
    if n % 2 == 0:
        m = n
    else:
        m = n + 1

    if n == 1 and k == 1:
        print('R')
    elif m/2 >= k:
        for i in range(n):
            if i%2 == 0 and k > c:
                newlst = lst.copy()
                newlst[b] = 'R'
                s = ''.join(newlst)
                b += 2
                c += 1
                print(s)
            else:
                s = ''.join(lst)
                print(s)
    else:
        print('-1')