def solve(k,sumV):
    global minV
    if k == N:
        if sumV < minV:
            minV = sumV
    elif sumV < minV:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = True
                solve(k+1, sumV + BRD[k][i])
                visited[i] = False

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    BRD = []
    for _ in range(N):
        BRD.append(list(map(int, input().split())))

    minV = 9 * N
    visited = [False] * N
    solve(0,0)
    print(f'#{tc} {minV}')