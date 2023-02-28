while 1:
    target = int(input())
    if target == -1:
        break
    ary=[]
    for i in range(1, target):
        if target % i == 0:
            ary.append(i)
    if sum(ary) == target:
        print(str(target) + " = " + " + ".join(map(str,ary)))
    else:
        print(str(target)+ " is NOT perfect.")