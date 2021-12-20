import sys
sys.stdin = open("1861_input.txt", "r")

def find(r, c, cnt, num):
    global maxV
    global startnum
    if maxV <= cnt:
        if maxV == cnt and startnum > num:
            startnum = num
        if maxV != cnt and startnum < num:
            startnum = num
        maxV = cnt
    for i in range(4):
        newr = r + dr[i]
        newc = c + dc[i]
        if 0 <= newr < N and 0<= newc < N and lst[newr][newc] - lst[r][c] == 1:
            cnt += 1
            find(newr, newc, cnt, num)
        else:
            pass

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

tc = int(input())

for t in range(1, tc+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    startnum = N**2

    for i in range(N):
        for j in range(N):
            find(i, j, 0, lst[i][j])
    
    print(f'#{t} {startnum} {maxV+1}')