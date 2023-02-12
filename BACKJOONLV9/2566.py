ary = ()
resultmx = -1
for i in range(1, 10):
    tmp = list(map(int, input().split()))
    tmpmx = max(tmp)
    if tmpmx>resultmx:
        resultmx = tmpmx
        ary = (i, tmp.index(tmpmx)+1)
print(resultmx)
print(*ary)