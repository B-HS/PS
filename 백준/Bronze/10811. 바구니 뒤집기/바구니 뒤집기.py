num, count = map(int, input().split())
ary = [k for k in range(1, num+1)]
for i in range(count):
    start, end = map(int, input().split())
    ary[start-1:end] = ary[start-1:end][::-1]
print(*ary)