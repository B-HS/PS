num = int(input())
for i in range(1, num+1):
    space = num-i
    print((' '*space)+'*'*((i*2)-1))

for i in range(num-1, -1, -1):
    space = num-i
    print((' '*space)+'*'*((i*2)-1))