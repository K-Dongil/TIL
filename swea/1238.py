def bfs(s):
    Q = []
    Q.append((1, s))
    visited[s] = True
    while Q:
        cnt, s = Q.pop(0)

        for i in range(1, 101):
            if lst[s][i] == 1 and not visited[i]:
                visited[i] = True
                Q.append((cnt+1, i))
                b.append((cnt+1,i))


for k in range(1, 11):
    data_len, start_point = map(int, input().split())
    input_lst = list(map(int, input().split()))
    lst = [[0]*101 for _ in range(101)]
    visited = [False]*101


    for i in range(0, data_len, 2):
        lst[input_lst[i]][input_lst[i+1]] = 1

    b = []
    bfs(start_point)

    print(f'#{k} {max(b)[1]}')