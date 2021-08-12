# 우, 하, 좌, 상
dx = []
dy = []
mode = 0, 1, 2, 3, 0, 1, 2, 3
mode += 1
if mode == 4:
    mode = 0

mode = (mode +1) %4

BRD = [[0]*N for _ in range(N)]

value = 1
curR = 0
curC = 0
while value <= N **2:
    BRD[curR][curC] = value

    #1. 좌표 갱신을 위하여 새로운 좌표가 유효한지 확인한다
    newR = curR + dy[mode]
    newC = curC + dx[mode]
    #2. 좌표가 유효하지 않으면 방향전환
    if newR < 0 or newR >= N or newC < 0 or newC >= N or BRD[newR][newC] != 0:
        mode = (mode + 1)% 4
    #3. 좌표를 갱신
    curR = curR + dy[mode]
    newC = curC + dx[mode]
    value += 1


while value <= N **2:
    value = newGetV()
    BRD[curR][curC] = value

    #1. 좌표 갱신을 위하여 새로운 좌표가 유효한지 확인한다
    newR = curR + dy[mode]
    newC = curC + dx[mode]
    #2. 좌표가 유효하지 않으면 방향전환
    if newR < 0 or newR >= N or newC < 0 or newC >= N or BRD[newR][newC] != 0:
        mode = (mode + 1)% 4
    #3. 좌표를 갱신
    curR = curR + dy[mode]
    newC = curC + dx[mode]
    value += 1