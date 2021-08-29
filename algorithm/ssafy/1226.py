def two_dimension_bfs(row, col):
    Q = []
    visited = [[0]*16 for _ in range(16)]
    Q.append((row, col))
    visited[row][col] = 1
    while Q:
        coordinates = Q.pop(0)
        row, col = coordinates[0], coordinates[1]
        if square[row][col] == 3:
            return 1
        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]
            if 0 <= nrow < 16 and 0 <= ncol < 16 and (square[nrow][ncol] ==0 or square[nrow][ncol] ==3) and visited[nrow][ncol] ==0:
                Q.append((nrow, ncol))
                visited[nrow][ncol] = visited[row][col] + 1
    return 0

def start_point(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] == 2:
                row = i
                col = j
    return row, col


dcol = [0, 0, 1, -1]
drow = [-1, 1, 0, 0]

for t in range(10):
    tc = int(input())
    square = [list(map(int, input())) for _ in range(16)]
    row, col = start_point(square)
    result = two_dimension_bfs(row,col)
    print('#{} {}'.format(t+1, result))