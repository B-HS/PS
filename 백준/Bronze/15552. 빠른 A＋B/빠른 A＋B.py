f=open(0).readlines()
for i in range(1,len(f)):print(sum(map(int,f[i].rstrip().split())))