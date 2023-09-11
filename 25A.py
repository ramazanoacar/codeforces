length = int(input())
x = input().split(" ")
even = 0
odd = 0
for i in range(3):
    if int(x[i]) % 2 == 0:
        even += 1
    else:
        odd += 1
search = 0
if even > odd:
    search = 1

for i in x:
    if int(i)%2 == search:
        print(x.index(i)+1)
        break


