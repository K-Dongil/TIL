def bfs(x, y):
    queue = [(x, y)]
    map[y][x] = 0
    cnt = 1

    while queue:
        nowX, nowY = queue.pop(0)
        
        for i in range(4):
            newX = nowX + dx[i]
            newY = nowY + dy[i]
            
            if 0<=newX<N and 0<=newY<N and map[newY][newX] == 1:
                queue.append((newX, newY))
                map[newY][newX] = 0
                cnt += 1

    return cnt

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

N = int(input())
map = [list(map(int, input())) for _ in range(N)]
apartments = []


for x in range(N):
    for y in range(N):
        if map[y][x] == 1:
            apartment = bfs(x, y)
            apartments.append(apartment)

apartments.sort()
apartments.insert(0, len(apartments))
for apartment in apartments:
    print(apartment)