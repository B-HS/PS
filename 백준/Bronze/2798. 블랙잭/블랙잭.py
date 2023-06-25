from itertools import combinations

num, target = map(int, input().split(" "))
ary = list(combinations(map(int, input().split(" ")), 3))
mx = 0

for i in ary:
    if sum(i) > mx and sum(i)<=target:
        mx = sum(i)

print(mx)


