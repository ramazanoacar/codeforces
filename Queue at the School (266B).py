x = input().split()
que = list(input())
for j in range(int(x[1])):
    a = 0
    for i in range(int(x[0])):
        if a + 2 > len(que):
            break
        if que[a] == 'B' and que[a+1] == 'G':
            que[a] = 'G'
            que[a+1] = 'B'
            a += 2
            continue
        a += 1
print(''.join(que))