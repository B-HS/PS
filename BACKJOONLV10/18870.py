import sys
sys.stdin.readline()
target= list(map(int, sys.stdin.readline().split()))
index_dic = sorted(list(set(target))) # 1000 999, 2 4 -10 -9
dic = {index_dic[i]:i for i in range(len(index_dic))}
for i in target:
    print(dic[i], end=" ")