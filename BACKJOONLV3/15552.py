f=open(0).readlines()
for i in range(1,len(f)):print(sum(map(int,f[i].rstrip().split())))

# stdin쓰면 
# import sys
# for i in range(int(sys.stdin.readline().rstrip())):
#     print(sum(map(int, sys.stdin.readline().rstrip().split())))