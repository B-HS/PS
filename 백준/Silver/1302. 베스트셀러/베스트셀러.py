from collections import Counter;
target = Counter([input() for _ in range(int(input()))]).most_common()
print(sorted(target,key=lambda x:(-int(x[1]),x[0]))[0][0])

# 백준에서 open(0) 코드가 잘 안먹나봄;; 
# from collections import Counter;
# print(sorted(Counter(open(0).read().split("\n")[1:]).most_common(),key=lambda x:(-int(x[1]),x[0]))[0][0])
