x = input().split()
k, n, w = int(x[0]), int(x[1]), int(x[2])
if int(w*(w+1)*k/2-n) < 0:
    print(0)
else:
    print(int(w*(w+1)*k/2-n))