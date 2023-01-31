target = int(input())
nums = list(input())
for i in nums[::-1]:
    print(target*int(i))
print(target*int("".join(nums)))