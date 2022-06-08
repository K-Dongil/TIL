def solve(k, sumV):
    global minV
    if k == N:
        if minV > sumV:
            minV = sumV
    elif sumV < minV:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                solve(k+1, sumV + lst[k][i])
                visited[i] = False


t = int(input())

for tc in range(1, t+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    minV = 99 * N

    solve(0,0)

    print(f'#{tc} {minV}')

