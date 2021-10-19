dr = [-1, 1, 0, 0, -1, 1, -1, 1] # 상하좌우, 대각선(좌상, 좌하, 우상, 우하)
dc = [0, 0, 1, -1, 1, 1, -1, -1]

tc = int(input())

for t in range(1, tc+1):
    boardSize, chance = map(int, input().split())
    board = [[0]*(boardSize+1) for _ in range(boardSize+1)]

    board[boardSize//2][boardSize//2] = 2
    board[boardSize//2 + 1][boardSize//2 + 1] = 2
    board[boardSize//2 + 1][boardSize//2] = 1
    board[boardSize//2][boardSize//2 + 1] = 1

    black = 0
    white = 0

    for i in range(chance):
        row, col, color = map(int, input().split())
        board[row][col] = color
        if color == 1:
            for i in range(8):
                sideR = row + dr[i]
                sideC = col + dc[i]
                if 1 <= sideR <= boardSize and 1 <= sideC <= boardSize and  board[sideR][sideC] == 2:
                    for j in range(2, boardSize):
                        side2R = row + dr[i] * j
                        side2C = col + dc[i] * j
                        if 1 <= side2R <= boardSize and 1 <= side2C <= boardSize and  board[side2R][side2C] == 0:
                            break
                        if 1 <= side2R <= boardSize and 1 <= side2C <= boardSize and  board[side2R][side2C] == 1:
                            for k in range(1, j-1):
                                a = row + dr[i] * k
                                b = col + dc[i] * k
                                board[a][b] = 1
                            break
        elif color == 2:
            for i in range(8):
                sideR = row + dr[i]
                sideC = col + dc[i]

                if 1 <= sideR <= boardSize and 1 <= sideC <= boardSize and  board[sideR][sideC] == 1:
                    for j in range(2, boardSize):
                        side2R = row + dr[i] * j
                        side2C = col + dc[i] * j
                        if 1 <= side2R <= boardSize and 1 <= side2C <= boardSize and  board[side2R][side2C] == 0:
                            break
                        if 1 <= side2R <= boardSize and 1 <= side2C <= boardSize and  board[side2R][side2C] == 2:
                            for k in range(1, j-1):
                                a = row + dr[i] * k
                                b = col + dc[i] * k
                                board[a][b] = 2
                            break
                    
    for lst in board:
        black += lst.count(1)
        white += lst.count(2)

    print(f'#{t} {black} {white}')