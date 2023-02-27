N, M = map(int, input().split())
target = [i for i in range(1, N+1)]
for _ in range(M):
    i, j, k = map(int, input().split())
    i, j, k = i-1, j-1, k-1
    target = target[:i] + target[k:j+1] + target[i:k] + target[j+1:]
print(*target)