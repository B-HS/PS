a, b  = map(int, input().split())
add = int(input())
minsum = (a*60)+b
added = minsum + add
rei = added//60
if rei >23:
    rei = rei-24
print (rei, (added%60))