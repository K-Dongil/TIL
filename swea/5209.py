def solve(k, sumV):
    global minV
    if minV <= sumV:
        return
    if k==N:
        if minV > sumV:
            minV = sumV
        return
    for i in range(N):
        if not used[i]:
            res[k] = i
            used[i] = True
            solve(k+1, sumV+lst[k][i])
            used[i] = False

tc = int(input())

for t in range(tc):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    res = [-1] * N
    used = [False] * N
    minV = 99 * N
    solve(0, 0)

    print(f'#{t+1} {minV}')