for _ in range(int(input())):
    num, word = input().split()
    for i in range(len(word)):
        print(word[i]*int(num), end="")
    print()