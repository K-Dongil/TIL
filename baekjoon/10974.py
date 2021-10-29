def solve(k):
    global N
    if k == N:
        results.append(' '.join(p))
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                p[k] = num_lst[i]
                solve(k+1)
                visited[i] = False 

N = int(input())
num_lst = list(range(1, N+1))
for i in range(len(num_lst)):
    num_lst[i] = str(num_lst[i])
visited = [False] * N
p = [0] * N
results = []
solve(0)

for result in results:
    print(result)