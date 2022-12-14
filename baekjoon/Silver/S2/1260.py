def dfs(v):
    visited = [False]*(nodeNum+1)
    st = [v]
    result = ''

    while st:
        nowNode = st.pop()
        if not visited[nowNode]:
            visited[nowNode] = True
            result += str(nowNode) + ' '
            for i in range(nodeNum, 0, -1):
                if graph[nowNode][i] == 1 and (not visited[i]):
                    st.append(i)

    return result

def bfs(v):
    visited = [False]*(nodeNum+1)
    visited[v] = True
    queue = [v]
    result = str(v)
    
    while queue:
        nowNode = queue.pop(0)
        for i in range(1, nodeNum+1):
            if graph[nowNode][i] == 1 and (not visited[i]):
                queue.append(i)
                visited[i] = True
                result += ' ' + str(i)

    return result

nodeNum, lineNum, start = map(int, input().split())
graph = [[0]*(nodeNum+1) for _ in range(nodeNum+1)]

for i in range(lineNum):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = 1
    graph[node2][node1] = 1

print(dfs(start))
print(bfs(start))