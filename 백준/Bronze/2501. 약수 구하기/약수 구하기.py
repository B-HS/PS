ary=[]
target, which = map(int, input().split())
cnt = 0
for i in range(1, target + 1):
    if target % i == 0:
        ary.append(i)
    cnt += 1

if which > len(ary):
    print(0)
else:
    print(ary[which-1])