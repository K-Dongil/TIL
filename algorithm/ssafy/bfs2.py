"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""


def bfs(s, V):  # s는 시작점
    q = [0]*V # 큐 생성
    front = -1
    rear = -1
    visited = [0]*(V+1) # visited 생성
    rear += 1 # 시작점 인큐
    q[rear] = s
    visited[s] = 1 # 시작점 visited
    while front != rear: # 큐가 비어있지 않다면
        front += 1 # 디큐해서 t에 저장
        t = q[front]
        print(t)
        for i in range(1, V+1): # t에 인접하고 미방문인 모든 i에 대해
            if adj[t][i] == 1 and visited[i] == 0:
                rear += 1 # 인큐 i
                q[rear] = i
                visited[i] = visited[t] + 1 # i 방문표시

V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0] * (V + 1) for _ in range(V + 1)]  # 인접 행렬

for i in range(E):
    n1, n2 = edge[2 * i], edge[2 * i + 1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1  # 방향이 없는 그래프

bfs(1, V)