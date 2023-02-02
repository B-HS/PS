target=open(0).readlines()
for i in target:
    print(sum(map(int,i.rstrip().split())))