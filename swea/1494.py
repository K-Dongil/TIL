import sys
sys.stdin = open("1.txt", "r")

def solve(x, y, k):
    global minV
    if k == N//2:
        curV = x*x + y*y
        if minV > curV:
            minV = curV
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                for j in range(N):
                    if not visited[j]:
                        visited[j] = True
                        solve(x+lst[j][0]-lst[i][0], y+lst[j][1]-lst[i][1], k+1)
                        visited[j] = False
                visited[i] = False

tc = int(input())

for t in range(1, tc+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    minV = 100000000000000000000
    solve(0, 0, 0)
    
    
    print(minV)