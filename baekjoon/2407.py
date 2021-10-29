# # nCr = n! / (r! * (n-r)!)
n, m = map(int, input().split())
dp = [0] * (n)
dp[0] = 1
dp[1] = 2

for i in range(3, n+1):
    dp[i-1] = dp[i-2] * i

nCr = dp[n-1] // (dp[m-1] * dp[n-m-1])
print(nCr)


# nCr = n! / (r! * (n-r)!)
n, m = map(int, input().split())
dp = [1] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] * i

nCr = dp[n] // (dp[m] * dp[n-m])
print(nCr) 
