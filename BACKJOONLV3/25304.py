target = int(input())
for i in range(int(input())):
    price, count = map(int, input().split())
    target -= price*count
if(target==0):
    print("Yes")
else:
    print("No")