def per(k):
    global minV
    if k==N:
        sumV = t
        if minV > sumV:
            minV = sumV

    else:
        for i in range(N):
            visited[i] = True
            t[k] = i
            per(k+1)
            visited[i] = False

t = [-1] * N
visited = [False] * N
minV = 10 * N