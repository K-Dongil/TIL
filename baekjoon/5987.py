def per(k):
    global cnt
    if k == N:
        for win, lose in win_info:
            if p.index(win) < p.index(lose):
                break
        else:
            cnt += 1
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                p[k] = player[i]
                per(k+1)
                visited[i] = False

tc = int(input())

for t in range(1, tc+1):
    N, M = map(int, input().split())
    player = list(range(1, N+1))
    win_info = [list(map(int, input().split())) for _ in range(M)]
    visited = [False] * N
    p = [0] * N
    cnt = 0
    per(0)

    print(f'#{t} {cnt}')