# m, n, target = map(int, input().split())
# count = 0
# result = 0
# while 1:
#     result += m
#     count += 1
#     if target <= result:
#         print(count)
#         break
#     result-=n
# 시간초과;;

m, n, slip = map(int,input().split())
per = m-n
target = slip-n

if target%per==0:
    print(target//per)
else:
    print(target//per+1)



