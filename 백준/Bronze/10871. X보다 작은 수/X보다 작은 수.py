a, target = map(int, input().split())
ary = map(int, input().split())

for i in ary:
    if i<target:
        print(i, end=" ")