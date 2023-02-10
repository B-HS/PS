def prime(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

prime_ary = []
for i in range(2, 246912):
    if prime(i):
        prime_ary.append(i)

while 1:
    target = int(input())
    if target==0:
        break
    cnt = 0
    end = target*2
    for i in prime_ary:
        if target < i <=end:
            cnt+=1
    print(cnt)