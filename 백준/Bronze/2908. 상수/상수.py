numa, numb = input().split()
print(numa[::-1] if int(numa[::-1])>int(numb[::-1]) else numb[::-1])