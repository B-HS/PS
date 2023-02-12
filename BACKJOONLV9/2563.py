ary = [[0]*100 for _ in range(100)]
for total in range(int(input())):
    x, y = map(int, input().split())
    for width in range(x, x+10):
        for height in range(y, y+10):
            ary[width][height] = 1
result = 0
for i in range(100):
    result += sum(ary[i])
print(result)
