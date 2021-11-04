import sys
sys.stdin = open("1.txt", "r")

def solve(row, col, direction, cnt):
    global now_move
    if min_move < cnt: # 백트래킹
        now_move = 100 * 100
        return
    if row == 99:
        now_move = cnt
    elif 0 <= row < 99 and 0 <= col < 99 and ladder[row][col+1] == 1 and (direction in ['down','right']):
        solve(row, col+1, 'right', cnt+1)
    elif 0 <= row < 99 and 0 < col <= 99 and ladder[row][col-1] == 1 and (direction in ['down', 'left']):
        solve(row, col-1, 'left', cnt+1)
    elif 0 <= row < 99 and 0 <= col <= 99 and  ladder[row+1][col] == 1:
        solve(row+1,col, 'down', cnt+1)

for t in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_move = 100 * 100
    find_point = 0
    now_move = 0

    for i in range(100):
        a = 0
        if ladder[0][i] == 1:
            solve(1, i, 'down', 1)
            if min_move >= now_move:
                min_move = now_move
                find_point = i
    
    print(f'#{t} {find_point}')