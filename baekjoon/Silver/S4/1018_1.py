def solve(x, y):
    whiteCnt = 0
    BlackCnt = 0

    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i+j) % 2:
                if board[j][i] == 'W':
                    BlackCnt += 1
                else:
                    whiteCnt += 1
            else:
                if board[j][i] == 'B':
                    BlackCnt += 1
                else:
                    whiteCnt += 1
                    
    return whiteCnt if whiteCnt <= BlackCnt else BlackCnt

height, width = map(int, input().split())
board = [input() for _ in range(height)]
startX = list(range(width-8+1))
startY = list(range(height-8+1))
result = 8*8

for X in startX:
    for Y in startY:
        changeV = solve(X, Y)
        if changeV < result:
            result = changeV

print(result)