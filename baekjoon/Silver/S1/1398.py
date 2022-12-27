def bfs(v):
    visited = [False] * (userNum+1)
    queue = [(v, 0)]
    visited[v] = True
    cnt = 0

    while queue:
        nowUser = queue.pop(0)
        for i in range(userNum+1):
            if visited[i] == False and graphs[nowUser[0]][i]:
                queue.append((i, nowUser[1]+1))
                visited[i] = True
                cnt += nowUser[1]+1

    return cnt

userNum, relationNum = map(int, input().split())
graphs = [[0]*(userNum+1) for _ in range(userNum+1)]
minkevinBacon = 100 * 6
winner = 0

for _ in range(relationNum):
    x, y = map(int, input().split())
    graphs[x][y] = 1
    graphs[y][x] = 1

for user in range(1, userNum+1):
    kevinBacon = bfs(user)
    if kevinBacon < minkevinBacon:
        minkevinBacon = kevinBacon
        winner = user

print(winner)