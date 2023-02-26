num, count = map(int, input().split())
ary = [k for k in range(1, num+1)]
for i in range(count):
    start, end = map(int, input().split())
    tmp1 = ary[start-1]
    tmp2 = ary[end-1]
    ary[start-1] = tmp2
    ary[end-1] = tmp1
print(*ary)