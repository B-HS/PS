in_list = list(map(int,open(0).read().split()))
for i in [k for k in range(1, 31)]:
    if i not in in_list:
        print(i)