x, y, w, h = map(int, input().split())
result = 1000
distanceList = [x, y, w-x, h-y]

for i in range(4):
    if distanceList[i] < result:
        result = distanceList[i]

print(result)