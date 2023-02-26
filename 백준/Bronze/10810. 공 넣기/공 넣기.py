num, count = map(int, input().split())
ary = [0 for k in range(1, num+1)]
for i in range(count):
    start, end, which = map(int, input().split())
    for j in range(start-1, end):
        ary[j] = which
print(*ary)