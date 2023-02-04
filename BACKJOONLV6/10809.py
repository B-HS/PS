ary = list(input())
for i in "abcdefghijklmnopqrstuvwxyz":
    if i in ary:
        print(ary.index(i), end=" ")
    else:
        print(-1, end=" ")