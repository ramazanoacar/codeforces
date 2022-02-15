n = int(input())
lst = []
for i in range(n):
    lst.append(input())
for i in lst:
    if len(i) <= 10:
        print(i)
    else:
        print(i[0]+ str(len(i) - 2) + i[len(i)-1])