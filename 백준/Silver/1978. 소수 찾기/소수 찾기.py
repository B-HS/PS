input()
ary = sorted(list(map(int, input().split())))
result = 0

for ele in ary:
    tmp = []
    if ele<2:
        continue
    for j in range(1, round(ele**(1/2)+1)):
        if ele%j == 0:
            tmp.append(j)
    if(len(tmp)==1):
        result+=1
print(result)
