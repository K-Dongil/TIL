def solve(k):
    global minV
    if k == N:
        res[-1] = 0
        sumV = 0
        for i in range(N):
            st = res[i]
            ed = res[i+1]
            sumV += ARR[st][ed]
        if minV > sumV:
            minV = sumV
        
        return 
    
    for i in range(N):
        if not visited[i]:
            res[k] = i
            visited[i] = True
            solve(k+1)
            visited[i] = False


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    res = [-1] * (N+1)

    
    visited = [False] * N
    res[0] = 0
    visited[0] = True
    minV = 123456789
    
    solve(1)