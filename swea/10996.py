# 지도:N*M크기, 물:W, 땅:L, 이동가능, 격자밖 이동 불가능
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1 , -1]

tc = int(input())

for t in range(1, tc+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    
    dist = [[987654321] * M for _ in range(N)] # 방문체크 겸 거리체크

    Q = deque()

    # 시작점인 물을 몽땅 담아두기 위해서
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "W":
                Q.append((i,j))
                dist[i][j] = 0

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            #if arr[nr][nc] == 'L' and dist[nr][nc] > dist[r][c] + 1:
            if arr[nr][nc] == 'L' and dist[nr][nc] == 987654321:
                dist[nr][nc] = dist[r][c] + 1
                Q.append((nr, nc))
        
    ans = 0

    for i in dist:
        for j in i:
            ans += j
    
    print(f'#{t} {ans}')
# =============================
dr = [-1, 1, 0, 0]
dc = [0, 0, 1 , -1]

tc = int(input())

for t in range(1, tc+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    
    dist = [[987654321] * M for _ in range(N)] # 방문체크 겸 거리체크

    Q = deque()
    Q = [0] * (N*M)
    front = -1
    rear = -1


    # 시작점인 물을 몽땅 담아두기 위해서
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "W":
                Q[rear] = (i,j)
                dist[i][j] = 0

    while front != rear:
        front += 1
        r, c = Q[front]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if arr[nr][nc] == 'L' and dist[nr][nc] == '987654321':
                dist[nr][nc] = dist[r][c] + 1
                rear += 1
                Q[rear] = (nr,nc)
        
    ans = 0

    for i in dist:
        for j in i:
            ans += j
    
    print(f'#{t} {ans}')

# #=============================
# # 지도:N*M크기, 물:W, 땅:L, 이동가능, 격자밖 이동 불가능
# def coordinate(str, N):
#     global ground
#     global water
#     for i in range(len(str)):
#         if str[i] == "L":
#             ground_xy[ground] = (N, i)
#             ground += 1 
#         elif str[i] == "W":
#             water_xy[water] = (N, i)
#             water += 1

# def min_len(tp):
#     distance = abs(water_xy[0][0] - tp[0]) + abs(water_xy[0][1] - tp[1])

#     for xy in water_xy:
#         x = abs(xy[0] - tp[0])
#         y = abs(xy[1] - tp[1])
#         min_xy = x+y
#         if distance > min_xy:
#             distance = min_xy

#     return distance


# tc = int(input())

# for t in range(tc):
#     N, M = map(int, input().split())
#     map_lst = [input() for _ in range(N)]
#     ground = 0
#     water = 0
#     water_count = 0
#     ground_count = 0
#     total_distance = 0

#     for m in map_lst:
#         water_count += m.count('W')
#         ground_count += m.count('L')
#     ground_xy = [0]*(ground_count)
#     water_xy = [0]*(water_count)

#     for i in range(len(map_lst)):
#         coordinate(map_lst[i], i)

#     for xy in ground_xy:
#         total_distance += min_len(xy)
    
#     print(f'#{t+1} {total_distance}')