input()
ary = input().split()
target = input()
result = 0
for i in ary:
    if i==target:
        result+=1
print(result)