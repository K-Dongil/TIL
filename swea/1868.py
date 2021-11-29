drow = [-1, -1, -1, 0, 0, 1, 1, 1] # 좌상, 상, 우상, 좌, 우, 좌하, 하, 우하
dcol = [1, 0, -1, 1, -1, 1, 0, -1]

drow2 = [-2, -2, -2, 0, 0, 2, 2, 2] # 좌상, 상, 우상, 좌, 우, 좌하, 하, 우하
dcol2 = [2, 0, -2, 2, -2, 2, 0, -2]

def solve(row, col, cnt):
    square[row][col] = 'C'
    for k in range(8):
        new_row = row + drow[k]
        new_col = col + dcol[k]
        if square[new_row][new_col] == '.':
            square[new_row][new_col] = 'C'
    for k in range(8):
        new_row = row + drow2[k]
        new_col = col + dcol2[k]
        if square[new_row][new_col] != '.':
            return
        solve(new_row, new_col, cnt+1)
    



tc = int(input())

for t in range(1, tc+1):
    square_size = int(input())
    square = [input().split() for _ in range(square_size)]
    min_count = 0

    for i in range(3):
        for j in range(3):
            if square[i][j] != '*':
                solve(i, j, 0)