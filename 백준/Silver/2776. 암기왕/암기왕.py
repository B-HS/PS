def binary_search(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2

        if list[mid] == target:
            return 1
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0

import sys
howmany = int(input())

for _ in range(howmany):
    input()
    target = sorted(list(map(int, sys.stdin.readline().split())))
    input()
    is_target = list(map(int, sys.stdin.readline().split()))
    
    for i in is_target:
        print(binary_search(target, i))
