target = int(input())
count = 0
while (1):
    if target%5==0:
        count+=(target//5)
        print(count)
        break
    count+=1
    target-=3
    if target<0:
        print(-1)
        break