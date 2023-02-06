a = int(input())
temp = 1
ans = 0
i = 1 
while(1):
    if a == 1:
        print (1)
        break
    elif 1< a <8:
        print (i+1)
        break
    elif a <= temp:
        print (i)
        break
    else:
        temp+=6*i
        i+=1
    
