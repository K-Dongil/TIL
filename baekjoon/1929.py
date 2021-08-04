N, M = map(int, input().split())
for i in range(N, M+1):
    divisor = 0
    for j in range(1, i+1):
        if not i%j:
            divisor += 1
    if divisor == 2:
        print(i)