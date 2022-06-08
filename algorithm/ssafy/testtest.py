def solve(k, color, cnt):
    global minV
    if k == (N-1):
        if minV > cnt and color != 0:
            minV = cnt
    else:
        for i in range(color, 3):
            if i == 0:
                paint = M - lst[k].count('W')
            elif i == 1:
                paint = M - lst[k].count('B')
            elif i == 2:
                paint = M - lst[k].count('R')
            solve(k+1, i, cnt+paint)

tc = int(input())

for t in range(1, tc+1):
    N, M = map(int, input().split())
    lst = [input().split() for _ in range(N)]
    a = lst[0].count('W')
    b = lst[0]
    first_line = M - lst[0].count('W')
    last_line = M - lst[N-1].count('R')
    minV = M * (N-2)
    solve(1, 0, 0)

    print(first_line+last_line+minV)