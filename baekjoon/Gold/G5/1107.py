nowChannel = 100
finishChannel = int(input())
brokenButtonNum = int(input())
brokenButtons = input().split() if brokenButtonNum else []
leastPress = abs(finishChannel - 100)

for num in range(999900):
    for n in str(num):
        if n in brokenButtons:
            break
    else:
        nowPress = len(str(num)) + abs(finishChannel - num)
        leastPress = nowPress if nowPress < leastPress else leastPress

print(leastPress)