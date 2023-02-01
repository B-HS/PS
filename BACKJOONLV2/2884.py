hh, mm = map(int, input().split())

if (mm-45<0):
    tmp = 60+mm-45
    if(hh==0):
        print(23, tmp)
    else:
        print(hh-1, tmp)
else:
    print(hh, mm-45)