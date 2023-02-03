for i in range(int(input())):
    tmp = list(map(int, input().split()))
    cnt = 0
    for j in tmp[1:]:
        if j>sum(tmp[1:])/tmp[0]:
            cnt+=1
    print("{:.3f}".format(cnt/tmp[0]*100))
    