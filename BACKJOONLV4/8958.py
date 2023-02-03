stg = []
result = 0
for i in range(int(input())):
    for k in input():
        if(k=="X"):
            result+= sum(stg)
            stg = []
        else:
            if(len(stg)==0):
                stg.append(1)
            else:
                stg.append(stg[-1]+1)
    result+=sum(stg)
    print(result)
    result = 0
    stg = []
