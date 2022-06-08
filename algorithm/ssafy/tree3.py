import sys
sys.stdin = open("1.txt", "r")
sys.setrecursionlimit(1000000)


drow = [-1, 1, 0, 0] # 상하좌우
dcol = [0, 0, -1, 1]

def solve(row, col, direction, cnt):
    global min_move
    global now_move
    newr = row + drow[direction]
    newc = col + dcol[direction]
    if row == 99:
        now_move = cnt
    elif 0 <= newr < 99 and 0 <= newc < 99 and ladder[newr][newc+1] == 1 and (direction in [1,3]):
        solve(newr, newc+1, 3, cnt+1)
    elif 0 <= newr < 99 and 0 <= newc < 99 and ladder[newr][newc-1] == 1 and (direction in [1, 2]):
        solve(newr, newc-1, 2, cnt+1)
    elif 0 <= newr < 99 and 0 <= newc < 99 and  ladder[newr][newc] == 1:
        solve(newr,newc, 1, cnt+1)

for t in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_move = 100 * 100
    find_point = 0
    now_move = 0

    for i in range(100):
        if ladder[0][i] == 1:
            solve(1, i, 1, 1)
            if min_move > now_move:
                min_move = now_move
                find_point = i

    print(find_point)