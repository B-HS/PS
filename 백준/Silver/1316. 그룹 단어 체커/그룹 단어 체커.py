result = 0
for i in range(int(input())):
    switch = True
    stg = []
    for k in input():
        if len(stg)!=0:
            if k in stg:
                if stg[-1]!=k:
                    switch = False
                else:
                    stg.append(k)
            else:
                stg.append(k)
        else:
            stg.append(k)
    if switch == True:
        result+=1
print(result)
                
            

