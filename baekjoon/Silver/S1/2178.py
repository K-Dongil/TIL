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
            if newX < 0 or width <= newX:
                continue
            elif newY < 0 or height <= newY:
                continue
            elif visited[newY][newX]:
                continue
            elif maze[newY][newX] == '0':
                continue
            
            queue.append((newX, newY, cnt+1))
    
    return cnt
        

height, width = map(int, input().split())
maze = [input() for _ in range(height)]

print(bfs(0,0))