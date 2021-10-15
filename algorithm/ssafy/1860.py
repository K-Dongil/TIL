TC = int(input())
for tc in range(1, TC+1):
    N, M, K = map(int, input().split())
    guest = list(map(int, input().split()))
    guest.sort()
    res = "Possible"
    for i in range(N):
        total = (guest[i]//M) * K
        if total < (i+1):
            res = "Impossible"
            break
    print('#{} {}'.format(tc, res))