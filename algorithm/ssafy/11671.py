import sys
sys.stdin = open("11671_input.txt", "r")

# x요소, y요소 제대로 볼것!
drow1 = [-1, 1, 0, 0] # 상하좌우
dcol1 = [0, 0, 1, -1]


drow2 = [-1, 1, 0, 0, -2, 2, 0, 0] # 상하좌우
dcol2 = [0, 0, 1, -1, 0, 0, 2, -2]

drow3 = [-1, 1, 0, 0, -2, 2, 0, 0, -3, 3, 0, 0] # 상하좌우
dcol3 = [0, 0, 1, -1, 0, 0, 2, -2, 0, 0, 3, -3]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if arr[row][col] == 'A':
                for i in range(4):
                    newr = row + drow1[i]
                    newc = col + dcol1[i]
                    if 0 <= newr < n and 0 <= newc < n and arr[newr][newc] == 'H':
                        arr[newr][newc] = 'X'
            elif arr[row][col] == 'B':
                for i in range(8):
                    newr = row + drow2[i]
                    newc = col + dcol2[i]
                    if 0 <= newr < n and 0 <= newc < n and arr[newr][newc] == 'H':
                        arr[newr][newc] = 'X'
            elif arr[row][col] == 'C':
                for i in range(12):
                    newr = row + drow3[i]
                    newc = col + dcol3[i]
                    if 0 <= newr < n and 0 <= newc < n and arr[newr][newc] == 'H':
                        arr[newr][newc] = 'X'
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')

"""
1
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
출력: #1 4 
"""

# def check(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 인덱스체크, H일때 X로 바꾸기
#         for j in range(ord(arr[x][y])-ord('A') + 1):
#             if 0 <= nx < N and 0 <= ny < N :
#                 if arr[nx][ny] == 'H':
#                     arr[nx][ny] = 'X'
#                 nx = nx + dx[i]
#                 ny = ny + dy[i]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(input()) for  in range(N)]
#
#     # 기지국 찾기
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] == 'C':
#                 check(i, j)
#     # 4방향 돌려서 커버되는 H -> X
#     # H 세기
#     ans = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 'H':
#                 ans += 1
#
#     print("#{} {}".format(tc, ans))
#     for i in arr:
#         print(*i)