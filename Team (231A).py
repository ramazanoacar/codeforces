n = int(input())
problems = []
answers = 0
for i in range(n):
    x = input().split()
    if int(x[0]) + int(x[1]) + int(x[2]) >= 2:
        answers += 1
print(answers)



