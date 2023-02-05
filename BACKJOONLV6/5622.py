target = ["0", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
word = input()
sum = 0
for i in range(1, len(target)):
    for z in word:
        if z in target[i]:
            sum +=i+2
print (sum)
