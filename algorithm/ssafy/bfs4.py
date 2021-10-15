# bfs 반복문 : 모든 vertex를 한번만 방문하여 출력
def bfs(s):
    Q = []
    Q.append(s)
    visited[s] = True
    while Q:
        s = Q.pop(0)
        print(s, end=' ')
        for i in grap[s]:
            if not visited[i]:
                Q.append(i)
                visited[i] = True

lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5 ,6, 6, 7 ,3, 7]
grap = [[] for _ in range(8)]
for i in range(0, len(lst), 2):
    s1 = lst[i]
    s2 = lst[i+1]
    grap[s1].append(s2)
    grap[s2].append(s1)


visited = [False] * 8
bfs(1)
