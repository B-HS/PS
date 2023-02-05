target = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
for i in target:
    word = word.replace(i, "0")
print(len(word))
