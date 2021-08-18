def dfs(s, V):
    visited = [0] * (V + 1)
    stack = [s]
    visited[s] = 1
    i = s  # 현재 방문한 정점 i
    print(node[i])
    while i != 0:  # True:
        for w in range(1, V + 1):
            if adj[i][w] == 1 and visited[w] == 0:
                stack.append(i)  # 반문 경로 저장
                i = w  # 새 방문지 이동
                visited[w] = 1
                print(node[w])
                break
        else:
            if stack:
                i = stack.pop()
            else:
                i = 0


adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0],  # A
       [0, 1, 0, 0, 1, 1, 0, 0],  # B
       [0, 1, 0, 0, 0, 1, 0, 0],  # C
       [0, 0, 1, 0, 0, 0, 1, 0],  # D
       [0, 0, 1, 1, 0, 0, 1, 0],  # E
       [0, 0, 0, 0, 1, 1, 0, 1],  # F
       [0, 0, 0, 0, 0, 0, 1, 0],  # G
       ]
node = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
dfs(1, 7)