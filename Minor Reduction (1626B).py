t = int(input())
for i in range(t):
    a = 0
    max = 0
    string_s = input()
    string = [int(x) for x in string_s]
    if len(string_s) == 1:
        print(string_s)
        continue
    for j in range(len(string)-2,-1,-1):
        if string[j] + string[j + 1] >= 10:
            string[j + 1] += string[j] - 10
            string[j] = 1
            a = 1
            break
    if a == 1:
        st = [str(x) for x in string]
        y = ''.join(st)
        print(y)
        continue
    print(str(int(string_s[0]) + int(string_s[1])) + string_s[2:])