def solve(direction):
    if direction == 'left':
        for i in range(gameSize):
            for j in range(gameSize):
                if games[i][j] == 0:
                    for k in range(j+1, gameSize):
                        if games[i][k] != 0:
                            games[i][j], games[i][k] = games[i][k], games[i][j]
                            break
            for j in range(gameSize-1):
                if games[i][j] == games[i][j+1]:
                    games[i][j] *= 2
                    games[i][j+1] = 0
            for j in range(gameSize):
                if games[i][j] == 0:
                    for k in range(j+1, gameSize):
                        if games[i][k] != 0:
                            games[i][j], games[i][k] = games[i][k], games[i][j]
                            break
    elif direction == 'right':
        for i in range(gameSize):
            for j in range(gameSize-1, -1, -1):
                if games[i][j] == 0:
                    for k in range(j-1, -1, -1):
                        if games[i][k] != 0:
                            games[i][j], games[i][k] = games[i][k], games[i][j]
                            break
            for j in range(gameSize-1, 0, -1):
                if games[i][j] == games[i][j-1]:
                    games[i][j] *= 2
                    games[i][j-1] = 0
            for j in range(gameSize-1, -1, -1):
                if games[i][j] == 0:
                    for k in range(j-1, -1, -1):
                        if games[i][k] != 0:
                            games[i][j], games[i][k] = games[i][k], games[i][j]
                            break
    elif direction == 'up':
        for i in range(gameSize):
            for j in range(gameSize):
                if games[j][i] == 0:
                    for k in range(j+1, gameSize):
                        if games[k][i] != 0:
                            games[j][i], games[k][i] = games[k][i], games[j][i]
                            break
            for j in range(gameSize-1):
                if games[j][i] == games[j+1][i]:
                    games[j][i] *= 2
                    games[j+1][i] = 0
            for j in range(gameSize):
                if games[j][i] == 0:
                    for k in range(j, gameSize):
                        if games[k][i] != 0:
                            games[j][i], games[k][i] = games[k][i], games[j][i]
                            break
    elif direction == 'down':
        for i in range(gameSize):
            for j in range(gameSize-1, -1, -1):
                if games[j][i] == 0:
                    for k in range(j-1, -1, -1):
                        if games[k][i] != 0:
                            games[j][i], games[k][i] = games[k][i], games[j][i]
                            break
            for j in range(gameSize-1, 0, -1):
                if games[j][i] == games[j-1][i]:
                    games[j][i] *= 2
                    games[j-1][i] = 0
            for j in range(gameSize-1, -1, -1):
                if games[j][i] == 0:
                    for k in range(j-1, -1, -1):
                        if games[k][i] != 0:
                            games[j][i], games[k][i] = games[k][i], games[j][i]
                            break

tc = int(input())

for t in range(1, tc+1):
    gameSize, direction = input().split()
    gameSize = int(gameSize)
    games = [list(map(int, input().split())) for _ in range(gameSize)]

    solve(direction)

    print(f'#{t}')
    for game in games:
        for l in game:
            print(l, end=' ')
        print()