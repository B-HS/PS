a=1;input()
def c(d):
    for i in range(2,int(k**0.5)+1):
        if d%i==0:return False
    return True
for k in set(map(int,input().split())):
    if c(k)==True:a*=k
print(a if a!=1 else -1)