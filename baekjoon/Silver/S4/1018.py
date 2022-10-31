def solution(idx, idy):
    cntW = 0
    cntB = 0
    for i in range(8): # 시작점 W
        for j in range(8):
            if (idx+idy+i+j)%2 == 0 and chess[idy+i][idx+j] == 'B':
                cntW += 1
            elif (idx+idy+i+j)%2 == 1 and chess[idy+i][idx+j] == 'W':
                cntW += 1
    
    for i in range(8): # 시작점 B
        for j in range(8):
            if (idx+idy+i+j)%2 == 0 and chess[idy+i][idx+j] == 'W':
                cntB += 1
            elif (idx+idy+i+j)%2 == 1 and chess[idy+i][idx+j] == 'B':
                cntB += 1
    
    return min(cntW, cntB)

vertical, width = map(int, input().split())
chess = [input() for _ in range(vertical)]
startX = list(range(width - 8 + 1))
startY = list(range(vertical - 8 + 1))
minV = 64

for x in startX:
    for y in startY:
        nowMinV = solution(x, y)
        if nowMinV < minV:
            minV = nowMinV

print(minV)