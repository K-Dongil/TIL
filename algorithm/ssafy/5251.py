tc = int(input())
for tc in range(1, tc+1):
    V, E = map(int, input().split())
    num = 9876543210
    graph = [[num for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        a, b, w = map(int, input().split())

        graph[a][b] = w

    dp = [num] * (V+1)
    dp[0] = 0

    for a in range(V+1):
        for b in range(V+1):
            if dp[a] + graph[a][b] < dp[b]:
                dp[b] = dp[a] + graph[a][b]

    answer = dp[V]
    print("#{} {}".format(tc, answer))