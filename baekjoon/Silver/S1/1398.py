def bfs(v):
    visited = [False] * (userNum+1)
    queue = [(v, 0)]
    cnt = 0

    while queue:
        nowUser = queue.pop()
        visited[nowUser[0]] = True
        for friend in graphs[nowUser[0]]:
            if visited[friend] == False:
                queue.append((friend, nowUser[1]+1))
                cnt += nowUser[1]+1

    return cnt

userNum, relationNum = map(int, input().split())
graphs = [[0]*(userNum+1) for _ in range(userNum+1)]

for _ in range(relationNum):
    x, y = map(int, input().split())
    graphs[x][y] = 1
    graphs[y][x] = 1

for user in range(1, userNum+1):
    print(bfs(user))