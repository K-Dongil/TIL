TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    BRD = [[0]*10 for _ in range(10) ]
    result = 0

    for cnt in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if color == 1:
                    if BRD[r][c] == 0:
                        BRD[r][c] = 1
                    elif BRD[r][c] == 2:
                        BRD[r][c] = 3
                        result += 1
                else:
                    if BRD[r][c] == 0:
                        BRD[r][c] = 2
                    elif BRD[r][c] == 1:
                        BRD[r][c] = 3
                        result += 1

    print('#{} {}'.format(test_case, result))


# =======================================
tc = int(input())

for t in range(1, tc+1):
    sqaureArea = [[0]*10 for _ in range(10)]
    squareNum = int(input())
    squares = [list(map(int, input().split())) for _ in range(squareNum)]
    total = 0

    for square in squares:
        color = square[4]
        leftX = square[0]
        leftY = square[1]
        rightX = square[2]
        rightY = square[3]

        if color == 1:
            for i in range(leftX, rightX+1):
                for j in range(leftY, rightY+1):
                    if sqaureArea[i][j] == 0:
                        sqaureArea[i][j] = 1
                    elif sqaureArea[i][j] == 2:
                        sqaureArea[i][j] = 3
                        total += 1
        if color == 2:
            for i in range(leftX, rightX+1):
                for j in range(leftY, rightY+1):
                    if sqaureArea[i][j] == 0:
                        sqaureArea[i][j] = 2
                    elif sqaureArea[i][j] == 1:
                        sqaureArea[i][j] = 3
                        total += 1
                    
    print('#{} {}'.format(t, total))