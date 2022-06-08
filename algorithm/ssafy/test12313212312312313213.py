def moveForGoal(r, c):
    global miro_len
    global result
    for i in range(4):
        newr = r + dr[i]
        newc = c + dc[i]

        if 0 <= newr < miro_len and 0 <= newc < miro_len and miro[newr][newc] == 3:
            result = '1'
        if 0 <= newr < miro_len and 0 <= newc < miro_len and (not visited[newr][newc]) and miro[newr][newc] == 0:
            visited[newr][newc] = 1
            moveForGoal(newr, newc)

dr = [0, 0, 1, -1]  # 상하좌우
dc = [-1, 1, 0, 0]

T = int(input())

for t in range(1, T+1):
    miro_len = int(input())
    miro = [list(map(int, input().split())) for _ in range(miro_len)]
    start_row = 0
    start_col = 0
    visited = [[0] * miro_len for _ in range(miro_len)]
    result = '0'

    # 출발지점 찾기
    for i in range(miro_len):
        for j in range(miro_len):
            if miro[i][j] == 2:
                start_row = i
                start_col = j

    moveForGoal(start_row, start_col)
    print('#{} {}'.format(t, result))