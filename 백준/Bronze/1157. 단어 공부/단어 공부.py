dict = {}
for i in input().lower():
    if dict.get(i)==None:
        dict[i] = 1
    else:
        dict[i] += 1
result_lambda = sorted(dict.items(), key=lambda x: x[1])
if dict.__len__()==1:
    print(list(dict.items())[0][0].upper())
    exit(0)
if result_lambda[::-1][0][1]==result_lambda[::-1][1][1]:
    print("?")
else:
    print(result_lambda[::-1][0][0].upper())
    