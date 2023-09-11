case_number = int(input())
for i in range(case_number):
    bag_no = int(input())
    odd = 0
    even = 0
    bags = input().split()
    for j in range(bag_no):
        candy = int(bags[j])
        if candy % 2 == 0:
            even += candy
        else:
            odd += candy
    if odd >= even:
        print("NO")
    else:
        print("YES")