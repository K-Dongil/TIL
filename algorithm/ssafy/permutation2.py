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
p = [0] * 3
arr = [1, 2, 3, 4, 5]
u = [0] * 5
f(3, 5, 0)