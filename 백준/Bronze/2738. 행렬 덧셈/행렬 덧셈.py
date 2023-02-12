width, height = map(int, input().split())
ary = []
for i in range(2):
    tmp = []
    for j in range(width):
        tmp.append(list(map(int, input().split())))
    ary.append(tmp)

for i in range(width):
    for j in range(height):
        print(ary[0][i][j] + ary[1][i][j], end=" ")
    print()
