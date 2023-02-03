ary = []
for _ in range(9):
    i = int(input())
    ary.append(i)

print (max(ary))
print (ary.index(max(ary))+1)