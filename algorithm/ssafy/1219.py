import sys
sys.stdin = open("1219_input.txt", "r")

def findw(v):
    for i in range(len(adj[v])):
        if adj[v][i] == 1 and visited[i] == False:
            return i
    return -1

def dfs(s, g):
    visited[s] = True
    #print(s)
    stack.append(s)
    while len(stack) > 0:
        w = findw(s)
        if w == g :
            return 1
        elif w != -1:
            stack.append(s)
            visited[w] = True
            #print(w)
            s = w
        else:
            s = stack.pop(-1)
    return 0


for t in range(10):
    tc, line = map(int, input().split())
    load_lst = list(map(int, input().split()))
    adj = [[0]*(100) for _ in range(100)]

    for i in range(0, len(load_lst)-1, 2):
        adj[load_lst[i]][load_lst[i+1]] = 1
        # 방향이 없을 때 adj[load_lst[i+1]][load_lst[i]] = 1

    visited = [False] * (100)
    stack = []
    result = dfs(0, 99)
    print('#{} {}'.format(tc, result))