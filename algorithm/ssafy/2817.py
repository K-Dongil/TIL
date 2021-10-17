def f(n, m, k): # n : 순열의 길이, k : 결정할 위치
    if n == k:
        print(p)
    else:
        for i in range(m):
            if u[i] == 0:
                u[i] = 1
                p[k] = arr[i]
                f(n, m, k+1)
                u[i] = 0

tc = int(input())

for t in range(tc):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [0] * len(arr)
    u = [0] * len(arr)
    f(3, len(arr), 0)
