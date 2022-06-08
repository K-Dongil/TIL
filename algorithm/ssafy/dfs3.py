# dfs 반복문 : 모든 vertex를 한번만 방문하여 출력
def dfs_f(s):
    ST = []
    ST.append(s)
    visited[s] = True
    while ST: # len(ST) > 0
        s = ST.pop(-1)
        print(s, end= '')
        for i in grap[s]:
            if not visited[i]:
                ST.append(i)
                visited[i] = True
    return

def dfs_f(s):
    ST = []
    ST.append(s)
    while ST: # len(ST) > 0
        s = ST.pop(-1)
        if not visited[s]:
            visited[s] = True
            print(s, end= '')
            for i in grap[s]:
                if not visited[i]:
                    ST.append(i)
    return

# dfs 재귀 : 모든 vertex를 한번만 방문하여 출력
def dfs_r(s):
    visited[s] = True
    print(s, end='')
    for i in grap[s]:
        if not visited[i]:
            dfs_r(i)

lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5 ,6, 6, 7 ,3, 7]
grap = [[] for _ in range(8)]
for i in range(0, len(lst), 2):
    s1 = lst[i]
    s2 = lst[i+1]
    grap[s1].append(s2)
    grap[s2].append(s1)


visited = [False] * 8
dfs_f(1)
print() # 1 3 7 6 5 4 2

visited = [False] * 8
dfs_r(1)
print() # 1 2 4 6 5 7 3

visited = [False] * 8