x = input().split()
k = int(x[1])
grades = input().split()
k_point = int(grades[k-1])
num = 0
for i in range(int(x[0])):
    if int(grades[i]) >= k_point and int(grades[i]) != 0 :
        num += 1
print(num)
