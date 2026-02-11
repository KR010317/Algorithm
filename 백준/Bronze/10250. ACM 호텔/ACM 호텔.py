t = int(input())
for i in range(t):
    h,w,n = input().split(' ')
    h,w,n = int(h), int(w), int(n)
    if n%h == 0:
        x = n//h
        if x < 10:
            x = '0' + str(x)
            print(str(h)+x)
        else:
            print(str(h)+str(x))
    else:
        if h > 1:
            y = str(n%h)
            x = str(n//h + 1)
            if int(x) < 10:
                x = '0' + x
                print(y+x)
            else:
                print(y+x)