di = [-1, 1, 0, 0] # 상하좌우
dj = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                print(arr[ni][nj])

# for i in range(N):
# 	for j in range(M):
# 		for dr, dc in [[0, 1], [1,0], [0, -1], [-1,0]]:
# 			ni = i + dr
# 			nj = j +dc
# 			if 0 <= ni < N and 0 <= nj < M:
# 				print(arr[ni][nj])