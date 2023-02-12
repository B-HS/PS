import sys

ary = [0]*10001
for i in range(int(sys.stdin.readline())):
    ary[int(sys.stdin.readline())] +=1

for i in range(len(ary)):
    if ary[i] >0:
        for p in range(ary[i]):
            print(i)