man, cut = map(int, input().split())
ary = sorted(list(map(int, input().split())))[::-1]
print(ary[cut-1])