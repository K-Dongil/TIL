# 연습문제 3
lst =[1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
G = {0:[], 1:[2, 3], 2:[1, 4, 5], 3:[1, 7], 4:[2, 6], 5:[2, 6], 6:[4, 5, 7], 7:[3, 5]}
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 1, 1, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 1],
       [0, 0, 1, 0, 0, 0, 1, 0],
       [0, 0, 1, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 1, 1, 0, 1],
       [0, 0, 0, 1, 0, 0, 1, 0]]


#=====================================================================
# lst =[1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# # v의 방문하지 않은 정점을 하나 찾아서 return한다
# # 방문하지 않은 정점이 없으면 -1을 return
# def findw(v):
#     for i in range(0, len(lst), 2):
#         if v == lst[i] and visited[lst[i+1]] ==False:
#             return lst[i+1]
#         if v == lst[i+1] and visited[lst[i]] ==False:
#             return lst[i]
#
#     return -1
#
# def dfs(v):
#     visited[v] = True
#     print(v)
#     stack.append(v)
#     while len(stack) > 0: # stack이
#         w = findw(v)
#         if w != -1:
#             stack.append(v)
#             visited[w] = True
#             print(w)
#             v = w
#         else:
#             v = stack.pop(-1)
#
# n = 7
# visited = [False] * (n+1) # n대신 n+1한 이유 : 0번 비워 놓는다
# stack = []
# dfs(1)
#
# #=====================================================================
# # v의 방문하지 않은 정점을 하나 찾아서 return한다
# # 방문하지 않은 정점이 없으면 -1을 return
# G = {0:[], 1:[2, 3], 2:[1, 4, 5], 3:[1, 7], 4:[2, 6], 5:[2, 6], 6:[4, 5, 7], 7:[3, 5]}
# def findw(v):
#     for w in G[v]:
#         if visited[w] == False:
#             return w
#     return -1
#
#
# def dfs(v):
#     visited[v] = True
#     print(v)
#     stack.append(v)
#     while len(stack) > 0: # stack이
#         w = findw(v)
#         if w != -1:
#             stack.append(v)
#             visited[w] = True
#             print(w)
#             v = w
#         else:
#             v = stack.pop(-1)
#
# n = 7
# visited = [False] * (n+1) # n대신 n+1한 이유 : 0번 비워 놓는다
# stack = []
# dfs(1)

#=====================================================================
# v의 방문하지 않은 정점을 하나 찾아서 return한다
# 방문하지 않은 정점이 없으면 -1을 return
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 1, 1, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 1],
       [0, 0, 1, 0, 0, 0, 1, 0],
       [0, 0, 1, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 1, 1, 0, 1],
       [0, 0, 0, 1, 0, 0, 1, 0]]
def findw(v):
    for i in range(len(adj[v])):
        if adj[v][i] == 1 and visited[i] == False:
            return i
    return -1
def findw(v):
    lst = adj[v]
    for i in range(len(lst)):
        if lst[i] == 1 and visited[i] == False:
            return i
    return -1

def dfs(v):
    visited[v] = True
    print(v)
    stack.append(v)
    while len(stack) > 0:  # stack이
        w = findw(v)
        if w != -1:
            stack.append(v)
            visited[w] = True
            print(w)
            v = w
        else:
            v = stack.pop(-1)
#
n = 7
visited = [False] * (n + 1)  # n대신 n+1한 이유 : 0번 비워 놓는다
stack = []
dfs(1)

#=====================================================================
G = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 5]]


# def dfs(v):
#     s = []
#     s.append(v)
#     while s:
#         v = s.pop(-1)
#         if not visited[v]:
#             print(v, end=' ')
#             visited[v] = True
#             for w in G[v]:
#                 if not visited[w]:
#                     s.append(w)


# def dfs(v):
#     s = []
#     s.append(v)
#     while s:
#         v = s.pop(-1)
#         print(v, end=' ')
#         for w in G[v]:
#             if not visited[w]:
#                 s.append(w)
#                 visited[w] = True


# def dfs(v):
#     visited[v] = True
#     print(v, end=' ')
#     for w in G[v]:
#         if not visited[w]:
#             dfs(w)


# visited = [False] * 8
# dfs(1)