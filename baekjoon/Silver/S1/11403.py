def dfs(v):
    st = [v]
    visited = [False] * N

    while st:
        nowNode = st.pop()
        if not visited[nowNode]:
            visited[nowNode] = True
            for i in range(N):
                if visited[i] == False and graph[nowNode][i] == '1':
                    st.append(i)
                    copyGraph[v][i] = '1'
                elif i == v and graph[nowNode][i] == '1':
                    copyGraph[v][i] = '1'

    return 0

N = int(input())
graph = [input().split() for _ in range(N)]
copyGraph = [['0']*N for _ in range(N)]
result = ''

for i in range(N):
    dfs(i)

for lst in copyGraph:
    result += ' '.join(lst) + '\n'

print(result)