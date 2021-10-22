t = int(input())
for tc in range(1, t + 1):
    N, A, B = map(int, input().split())
    result = B * (N - 1)
 
    for c in range(1, N//2):
        for r in range(c, N):
            if N < r * c:
                break
            temp = A * (r - c) + B * (N - r * c)
            if temp < result:
                result = temp
    print('#{} {}'.format(tc, result))