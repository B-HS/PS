fullset = [1, 1, 2, 2, 2, 8]
for i, ele in enumerate(map(int, input().split(" "))):
    fullset[i]-=ele
print(" ".join(map(str, fullset)))