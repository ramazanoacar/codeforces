x = list(input())
low, upp = 0, 0
for i in x:
    if i.islower():
        low += 1
        continue
    upp += 1
s = ''.join(x)
if upp <= low:
    print(s.lower())
else:
    print(s.upper())