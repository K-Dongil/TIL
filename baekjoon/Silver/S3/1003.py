t = int(input())
numList = [int(input()) for _ in range(t)]
maxNum = max(numList)
dp = [[0, 0] for _ in range(maxNum+1)]
dp[0][0] = 1
if maxNum != 0:
    dp[1][1] = 1

for i in range(2, maxNum+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for num in numList:
    print('{} {}'.format(dp[num][0], dp[num][1]))