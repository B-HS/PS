m, n, slip = map(int,input().split())
per = m-n
target = slip-n

if target%per==0:
    print(target//per)
else:
    print(target//per+1)