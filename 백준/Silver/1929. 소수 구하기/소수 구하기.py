lw, hg = map(int, input().split())
ary = [i for i in range(lw, hg+1)]

for ele in ary:
    switch = False
    if ele<2:
        continue
    for j in range(2, round(ele**(1/2)+1)):
        if ele%j == 0:
            switch = True
            break
    if(switch==False):
        print(ele)
