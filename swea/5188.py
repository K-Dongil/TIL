def solve(curX, curY, sumV):
    global minV
    if curX == N-1 and curY == N-1:
        if minV > sumV:
            minV = sumV
        return
    if curX+1 < N:
        solve(curX+1, curY, sumV+ARR[curY][curX+1])
    if curY+1 < N:
        solve(curX, curY+1, sumV + ARR[curY+1][curX])

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    minV = N*N*10
    solve(0, 0, ARR[0][0])

    print(f'#{tc} {minV}')