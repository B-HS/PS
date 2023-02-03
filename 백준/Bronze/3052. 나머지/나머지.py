list = []
for i in range(10):
    list.append(int(input()))
result = set()
for i in list:
    result.add(i%42)
print(len(result))