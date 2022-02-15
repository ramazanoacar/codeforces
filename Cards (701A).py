n = int(input())
lst_s = input().split()
lst = []
index_lst = []
total = 0
for i in range(len(lst_s)):
    lst.append(int(lst_s[i]))
    total += int((lst_s[i]))
x = 2 * total / n
for j in range(len(lst_s)):
    if j not in index_lst:
        y = x - lst[j]
        index_lst.append(j)
        while True:
            ind = lst.index(y)
            if ind in index_lst:
                lst.insert(ind,'a')
                lst.remove(y)
                continue
            break
        index_lst.append(ind)
b = 0
for i in range(int(len(lst_s)/2)):
    print(index_lst[b] + 1,end=' ')
    print((index_lst[b+1]+1))
    b += 2