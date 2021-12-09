# 교수님 풀이
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def DFS(r, c, line):
    if len(line) == 7:
        ans.append(line)
        return
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        DFS(nr, nc, line+arr[nr][nc])

T = int(input())

for tc in range(1, T+1):
    N = 4
    arr = [input().split() for _ in range(N)]

    ans = []

    for i in range(N):
        for j in range(N):
            DFS(i, j, arr[i][j])
    
    print(f'#{tc} {len(ans)}')

#===============================================
# def DFS(r, c, num, idx): # 좌표, 만들고 있는 숫자, 어디자리까지 만들었는지
#     if idx == 7:
#         ans.add(num)
#     else:
#         for i in range(4):
#             nr, nc = r + dr[i], c + dc[i]

#             if 0 <= nr < N and 0 <= nc < N:
#                 DFS(nr, nc, num * 10 + arr[nr][nc], idx+1)
                
# T = int(input())

# for tc in range(1, T+1):
#     N = 4
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     ans = set()

#     for i in range(N):
#         for j in range(N):
#             DFS(i, j, arr[i][j])
    
#     print(f'#{tc} {len(ans)}')