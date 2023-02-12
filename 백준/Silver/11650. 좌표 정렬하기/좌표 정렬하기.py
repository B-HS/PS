ary = []
for i in range(int(input())):
    x, y = map(int, input().split())
    ary.append([x, y])
ary.sort(key=lambda x: (x[0], x[1]))
for i in ary:
    print(*i)