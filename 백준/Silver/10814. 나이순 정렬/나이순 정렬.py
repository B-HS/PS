ary=[]
for i in range(int(input())):
    age, name = input().split()
    ary.append([int(age), name])
ary.sort(key=lambda x:x[0])
for i in ary:
    print(*i)
