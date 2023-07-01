ary = []
for i in range(int(input())):ary.append(input().split())
ary.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(ary[-1][0],ary[0][0],sep='\n')

# 아래코드는 왜 index오류인지 모르겠음
# ary=sorted([i.split() for i in open(0).read().split("\n")[1:]],key=lambda x:(int(x[3]),int(x[2]),int(x[1])))
# print(ary[-1][0],ary[0][0],sep='\n')
