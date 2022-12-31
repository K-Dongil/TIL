width = int(input())
dp = [1] * (width+1)

if 2 <= width:
    dp[2] = 3

for i in range(3, width+1):
    dp[i] = dp[i-1] + 2*dp[i-2]

print(dp[width]%10007)