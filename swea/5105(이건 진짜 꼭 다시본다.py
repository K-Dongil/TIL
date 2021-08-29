def two_dimension_bfs(row, col):
    Q = []
    visited = [[0]*square_size for _ in range(square_size)]
    Q.append((row, col))
    visited[row][col] = 1
    while Q:
        coordinates = Q.pop(0)
        row, col = coordinates[0], coordinates[1]
        if square[row][col] == 3:
            return visited[row][col] - 2
        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]
            if 0 <= nrow < square_size and 0 <= ncol < square_size and (square[nrow][ncol] ==0 or square[nrow][ncol] ==3) and visited[nrow][ncol] ==0:
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

tc = int(input())

dcol = [0, 0, 1, -1]
drow = [-1, 1, 0, 0]

for t in range(tc):
    square_size = int(input())
    square = [list(map(int, input())) for _ in range(square_size)]
    row, col = start_point(square)
    result = two_dimension_bfs(row,col)
    print('#{} {}'.format(t+1, result))



# =========================================================================================
# 교수님 코드 visited 이용X
def two_dimension_bfs(row, col):
    Q = []
    Q.append((row, col))
    square[row][col] = 0 # '0'하고 구분할 것
    while Q:
        coordinates = Q.pop(0)
        row, col = coordinates[0], coordinates[1]
        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]
            if 0 <= nrow < square_size and 0 <= ncol < square_size and (square[nrow][ncol] == '0' or square[nrow][ncol] == '3'):
                if square[nrow][ncol] == '3':
                    return square[row][col]
                if square[nrow][ncol] == '0':
                    Q.append((nrow, ncol))
                    square[nrow][ncol] = square[row][col] + 1
    return 0

def start_point(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] == '2':
                row = i
                col = j
    return row, col

tc = int(input())

dcol = [0, 0, 1, -1]
drow = [-1, 1, 0, 0]

for t in range(tc):
    square_size = int(input())
    square = [list(input()) for _ in range(square_size)]
    row, col = start_point(square)
    result = two_dimension_bfs(row,col)
    print('#{} {}'.format(t+1, result))