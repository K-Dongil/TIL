from collections import deque

def solve():
    Q = deque()
    Q.append((0,0))
    D[0][0] = 0

    while Q:
        curX, curY = Q.popleft()
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            newX = curX + dx
            newY = curY + dy
            if 0 <= newX < N and 0 <= newY < N:

                # if ARR[newY][newX] > ARR[curY][curX]
                #     fuel = Arr[newY][newX] -Arr[curY][curX] + 1
                # else:
                #     fuel = 1
                fuel = max(ARR[newY][newX] -ARR[curY][curX], 0) + 1

                #D[newY][newX] = min(D[newY][newX], D[curY][curX] + fuel)
                if D[newY][newX] > D[curY][curX]+fuel:
                    D[newY][newX] = D[curY][curX] + fuel
                    Q.append((newX, newY))

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    D = [[N*N*1000] * N  for _ in range(N)]
    solve()

    print('#{} {}'.format(tc, D[N - 1][N - 1]))