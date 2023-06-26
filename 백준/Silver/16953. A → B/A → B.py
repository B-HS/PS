start, end = list(map(int, input().split(" ")))
cnt = 1
while 1 :
    failcnt = 0
    if(start== end):
        break
    if(str(end/2).split(".")[1] == "0"):
        end //= 2
        cnt+=1
    else:
        failcnt+=1
    if(len(str(end))>1 and str(end)[-1] == "1"):
        end  = int(str(end)[:-1])
        cnt+=1
    else:
        failcnt+=1
    if(start > end or failcnt ==2):
        cnt = -1
        break
print(cnt)