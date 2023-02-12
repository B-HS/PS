from collections import Counter
import sys
ary = sorted([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))])
print(round(sum(ary)/len(ary)))
print(ary[len(ary)//2])

cnt = Counter(ary).most_common(2) #mxcnt -2
if len(cnt)>1:
    if cnt[0][1] == cnt[1][1]: 
        print(cnt[1][0]) 
    else: 
        print(cnt[0][0])
else: 
    print(cnt[0][0])

print(abs(ary[0]-ary[-1]))