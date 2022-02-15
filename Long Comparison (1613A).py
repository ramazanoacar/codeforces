t = int(input())
while t > 0:
    x = input().split()
    y = input().split()
    if len(x[0]) + int(x[1]) > len(y[0]) + int(y[1]):
        print('>')
    elif len(x[0]) + int(x[1]) < len(y[0]) + int(y[1]):
        print('<')
    else:
        if len(x[0]) == len(y[0]):
            if int(x[0]) > int(y[0]):
                print('>')
            elif int(x[0]) < int(y[0]):
                print('<')
            else:
                print('=')
            t -= 1
            continue
        if int(x[1]) > int(y[1]):
            y1 = list(y[0])
            y1.insert(-(int(x[1])-int(y[1])),'.')
            ys = ''.join(y1)
            yi = float(ys)
            if int(x[0]) > yi:
                print('>')
            elif int(x[0]) < yi:
                print('<')
            else:
                print('=')
        elif int(x[1]) < int(y[1]):
            x1 = list(x[0])
            x1.insert(-(int(y[1]) - int(x[1])), '.')
            xs = ''.join(x1)
            xi = float(xs)
            if int(y[0]) > xi:
                print('<')
            elif int(y[0]) < xi:
                print('>')
            else:
                print('=')
        else:
            print('=')
    t -= 1