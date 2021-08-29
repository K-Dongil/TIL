def dfs(v):
    ST = []
    visited = [False] * 8

    ST.append(v)
    visited[v] = True

    while ST:
        v = ST.pop(-1)
        print(v, end= ' ')
        for w in G[v]:
            if not visited[w]:
                ST.append(w)
                visited[w] = True


def bfs_adj(v):
    Q = []
    visited = [False] * 8

    Q.append(v)
    visited[v] = True

    while Q:
        v = Q.pop(0)
        print(v, end= ' ')

        for w in range(len(adj[v])):
            if adj[v][w] == 1 and not visited[w]:
                Q.append(w)
                visited[w] = True

def bfs_G(v):
    Q = []
    visited = [0] * 8
    Q.append(v)
    # 첫번째 것 무조건 큐에 넣는다.
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        print(v, visited[v])
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1

lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
G = [[] for _ in range(8)]
adj = [[0] * 8 for _ in range(8)]

for i in range(0,16, 2):
    v1 = lst[i]
    v2 = lst[i+1]

    G[v1].append(v2)
    G[v2].append(v1)

    adj[v1][v2] = 1
    adj[v2][v1] = 1

bfs_adj(1)
print()
bfs_G(1)
print()
dfs(1)