target = input()
ans = 0
for i in range(int(target)+1):
    result = int(i) + sum(map(int, str(i).strip()))
    if str(result) == target:
        ans = i 
        break
print(ans)