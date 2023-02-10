import sys
input = sys.stdin.readline
ary = [False]*10001
for i in range(2, 10001):
    cnt =0
    for p in range(2, int(i**0.5)+1):
        if i%p ==0:
            cnt=1
    if cnt ==0:
        ary[i]=True
num = int(input())
for i in range(num):
    a = int(input())
    b= a//2
    for p in range(b, 1, -1):
        if ary[a-p] == True and ary[p]==True:
            print(p, a-p)
            break