startPoint =  { # 상하좌우, 시작 끝 i j
    'up':[0, 0], 'down':[0, 0],
    'left':[0, -1], 'right':[0, 0]
}

def solve():
    for i in range(gameSize):
        for j in range(gameSize-1):
            if game[i][j] == game[i][j+1]:
                game[i][j] *= 2
                game[i][j+1] = 0

tc = int(input())

for t in range(1, tc+1):
    gameSize, direction = input().split()
    game = [list(map(int, input().split())) for _ in range(gameSize)]

    solve(direction)



# def solve():
#     # trueFalse = True
#     for i in range(gameSize-1):
#         for j in range(gameSize-1):
#             # if trueFalse:
#             if game[i][j] == game[i][j+1]:
#                 game[i][j] *= 2
#                 game[i][j+1] = 0
#             # else:
#             #     trueFalse = False