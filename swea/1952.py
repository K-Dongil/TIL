# 1day:10, 1month:40, 3month:100, 1year:300
def calc(cost, m):
    global min_cost
    if m > 12:
        if min_cost > cost:
            min_cost = cost
        return
    # 1일권
    calc(cost + day*schedule[m], m+1)
    # 1달권
    calc(cost + month, m+1)
    # 3갈권
    calc(cost + month3, m+3)


tc = int(input())

for t in range(tc):
    day, month, month3, year = map(int, input().split())
    schedule = [0] + list(map(int, input().split()))
    min_cost = year # 1년치 비용이 현재 최저의 가격

    calc(0, 1)
    print(f'#{t+1} {min_cost}')

# DP###########################################################################
tc = int(input())

for t in range(tc):
    day, month, month3, year = map(int, input().split())
    schedule = [0] + list(map(int, input().split()))
    min_cost = year # 1년치 비용이 현재 최저의 가격

    dp = [0] * 13 # 해당 월까지의 최소값이 저장이 되어있음

    dp[1] = min(month, schedule[1] * day)
    dp[2] = dp[1] + min(month, schedule[1] * day)

    for i in range(3, 13):
        dp[i] = min(dp[i-3] + month3, dp[i-1] + month, dp[i-1] + schedule[i]*day)

    print(f'#{t+1} {min(dp[12], year)}')