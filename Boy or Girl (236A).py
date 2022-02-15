x = list(input())
counts = []
for i in x:
    if i not in counts:
        counts.append(i)
if len(counts)%2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')