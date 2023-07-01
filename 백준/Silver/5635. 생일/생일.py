ary = []
for i in range(int(input())):ary.append(input().split())
ary.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(ary[-1][0],ary[0][0],sep='\n')