targets = [sorted([*map(int, input().split())])[1:-1] for _ in range(int(input()))]
for i in targets:
    if i[-1] - i[0]>=4:
        print("KIN")
    else:
        print(sum(i))