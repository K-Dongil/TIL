def bfs(s, f):
    q = []
    visited = [0] * (node+1)
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop(0)

        for i in range(1, node+1):
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1
                if i == f:
                    return visited[i] - 1
    return 0

tc = int(input())

for t in range(tc):
    node, line = map(int, input().split())
    adj = [[0]*(node+1) for _ in range(node+1)]

    for i in range(line):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1

    s_node, f_node = map(int, input().split())
    result = bfs(s_node, f_node)
    print('#{} {}'.format(t+1, result))