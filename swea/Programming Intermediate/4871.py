def dfs(start, end, V):
    visited= [False] * (nodeNum+1)
    st = [start]
    nowNode = start
    visited[start] = True

    while nowNode != end:
        for i in range(1, V+1):
            if lst[nowNode][i] == 1 and visited[i] == False:
                st.append(i)
                nowNode = i
                visited[i] = True
                break
        else:
            if st:
                nowNode = st.pop()
            else:
                return 0

        if nowNode == end:
            return 1

    return 0

tc = int(input())

for t in range(1, tc+1):
    nodeNum, lineNum = map(int, input().split())
    lst = [[0]*(nodeNum+1) for _ in range(nodeNum+1)]
    result = 0

    for i in range(lineNum):
        startNode, endNode = map(int, input().split())
        lst[startNode][endNode] = 1
    
    startNode, endNode = map(int, input().split())
    result = dfs(startNode, endNode, nodeNum)

    print('#{} {}'.format(t, result))