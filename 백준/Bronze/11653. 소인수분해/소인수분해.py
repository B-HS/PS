num = int(input())
i = 2
#2부터 없애가며 쫙내려가기
while(1):
    if num%i == 0:
        print (i)
        num = num/i
        i = 2
    else:
        i += 1
    if num == 1:
        break