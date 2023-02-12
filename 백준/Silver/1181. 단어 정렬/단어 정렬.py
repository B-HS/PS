ary=list(set(input() for _ in range(int(input()))))
ary.sort(key=lambda x:(len(x),x))
print(*ary,sep="\n")
