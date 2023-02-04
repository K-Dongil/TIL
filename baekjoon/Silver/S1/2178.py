from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    visited = [[False]*width for _ in range(height)]
    queue = deque()
    queue.append((x, y, 1))
    cnt = 0

    while queue:
        x, y, cnt = queue.popleft()
        visited[y][x] = True

        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < width and 0 <= newY < height and visited[newY][newX] == False and maze[newY][newX] == '1':
                queue.append((newX, newY, cnt+1))
    
    return cnt
        

height, width = map(int, input().split())
maze = [input() for _ in range(height)]

print(bfs(0,0))