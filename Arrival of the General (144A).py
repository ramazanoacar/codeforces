n = int(input())
lst_str = input().split()
lst = []
for i in range(n):
    lst.append(int(lst_str[i]))
min, max = None, None
for j in range(n):
    if max is None or lst[j] > max:
        max = lst[j]
        max_index = j
    if min is None or lst[n-j-1] < min:
        min = lst[n-j-1]
        min_index = n-j-1
if min_index < max_index:
    print(max_index + n - min_index - 2)
else:
    print(max_index + n - min_index - 1)