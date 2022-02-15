x = int(input())
stops = []
max,count = None, 0
for i in range(x):
    y = input().split()
    count += int(y[1])-int(y[0])
    if max is None or count > max:
        max = count
print(max)
