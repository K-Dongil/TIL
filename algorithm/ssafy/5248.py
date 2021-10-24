# DFS
# dfs 재귀 : 모든 vertex를 한번만 방문하여 출력
def dfs(curV):
    visited[curV] = True

    for newV in G[curV]:
        if not visited[newV]:
            dfs(newV)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    G = [[] for _ in range(N+1)]

    for i in range(M):
        s1 = lst[i*2]
        s2 = lst[i*2+1]
        G[s1].append(s2)
        G[s2].append(s1)

    cnt = 0
    visited = [False] * (N+1)
    for i in range(1, N+1):
        if not visited[i]:
            dfs(1)
            cnt += 1

    print(f'#{tc} {cnt}')

###############################################################
# 서로소??
def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    p = [i for i in range(N+1)]

    for i in range(M):
        s1 = lst[i*2]
        s2 = lst[i*2+1]
        union(s1, s2)

    cnt = [0] * (N+1)
    for i in range(1, N+1):
        cnt[find_set(i)] = 1

    print(f'#{tc} {sum(cnt)}')