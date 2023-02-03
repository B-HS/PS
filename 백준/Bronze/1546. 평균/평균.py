i=open(0).readlines()
ary = sorted(list(map(int,i[1].split())))
mx = max(ary)
tmp = 0
for k in ary:
    tmp +=k/mx*100
print(tmp/int(i[0].rstrip()))