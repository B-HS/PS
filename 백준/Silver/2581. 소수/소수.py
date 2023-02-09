lw, hg = map(int, open(0).read().rstrip().split())
ary = [i for i in range(lw, hg+1)][::-1]
result = 0
min_result = 0
for ele in ary:
    tmp = []
    if ele<2:
        continue
    for j in range(1, round(ele**(1/2)+1)):
        if ele%j == 0:
            tmp.append(j)
    if(len(tmp)==1):
        result+=ele
        min_result=ele

if result+min_result == 0:
    print(-1)
else:
    print(result)
    print(min_result)
