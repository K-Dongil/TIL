def dfs(v):
    visited = [False] * (computerNum+1)
    st = [v]
    virus = -1 # 1번 텀퓨터는 제외

    while st:
        nowNode = st.pop()
        if not visited[nowNode]:
            visited[nowNode] = True
            virus += 1
            for i in range(1, computerNum+1):
                if computers[nowNode][i] and not visited[i]:
                    st.append(i)

    return virus

computerNum = int(input())
relations = int(input())
computers = [[0]*(computerNum+1) for _ in range(computerNum+1)]

for _ in range(relations):
    leftNode, rightNode = map(int, input().split())
    computers[leftNode][rightNode] = computers[rightNode][leftNode] = 1

print(dfs(1))