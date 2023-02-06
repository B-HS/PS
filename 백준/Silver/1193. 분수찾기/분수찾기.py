num = int(input())
tempnum = 0 
tmp=0 
while(1):
    tempnum = tmp+tempnum
    if tempnum>=num:
        break
    tmp+=1
where = tempnum - num 
if tmp %2 !=0:
    print(str(1+where)+"/"+str(tmp-where))
else: 
    print(str(tmp-where)+"/"+str(1+where))
