num = int(input())
tmp = num
count = 0
while(1):
    ten = tmp//10
    one = tmp%10
    sum = int(ten)+int(one)
    tmp = int(str(tmp%10)+str(sum%10))
    count = count +1
    if (tmp==num):break

print(count)