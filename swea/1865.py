def solve(k, sumV):
    global maxV
    if maxV >= sumV:
        return
    if k==N:
        if maxV < sumV:
            maxV = sumV
        return
    for i in range(N):
        if not used[i]:
            res[k] = i
            used[i] = True
            solve(k+1, sumV*(lst[k][i]/100))
            used[i] = False

tc = int(input())

for t in range(tc):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    res = [-1] * N
    used = [False] * N
    maxV = 0
    solve(0, 1)
    maxV = format(maxV*100, '.6f')

    print('#{} {}'.format(t+1, maxV))