def comb(n, r):
    global minV
    global B
    if r == 0:
        if minV > sum(T) and sum(T) >= B:
            minV = sum(T)
    elif n < r:
        return
    else:
        T[r - 1] = heights[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)

tc = int(input())

for t in range(1, tc+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    length = len(heights)
    T = [0] * length
    minV = 20 * 10000
    for i in range(1, length+1):
        comb(length, i)
    
    print(f'#{t} {minV - B}')