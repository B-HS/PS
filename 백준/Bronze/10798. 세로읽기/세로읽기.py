target = {}
ary = open(0).read().split("\n")
for i in ary:
    for j in range(1, len(i)+1):
        if target.get(str(j))!=None:
            target[str(j)] += i[j-1]
        else:
            target[str(j)] = i[j-1]
print("".join(target.values()))