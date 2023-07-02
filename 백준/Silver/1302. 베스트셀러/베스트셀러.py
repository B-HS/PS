from collections import Counter;
target = Counter([input() for _ in range(int(input()))]).most_common()
print(sorted(target,key=lambda x:(-int(x[1]),x[0]))[0][0])