x = int(input())
y = list(input())
count,a = 0,0
for i in range(x):
    if i == x - 1:
        break
    if y[i] == y[i+1]:
        count += 1
print(count)

