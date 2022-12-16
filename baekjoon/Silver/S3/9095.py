T = int(input())
numList = [int(input()) for _ in range(T)]
dp = [0]*(11) # 입력값은 11보다 작다
dp[1] = 1 # 1
dp[2] = 2 # 1+1, 2
dp[3] = 4 # 1+1+1, 1+2, 2+1, 3

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for num in numList:
    print(dp[num])

'''
입력값 범위가 안 정해져 있을 때
T = int(input())
numList = [int(input()) for _ in range(T)]
maxNum = max(numList)
dp = [0]*(maxNum+1 if 4 <= maxNum else 4)
dp[1] = 1 # 1
dp[2] = 2 # 1+1, 2
dp[3] = 4 # 1+1+1, 1+2, 2+1, 3

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for num in numList:
    print(dp[num])
'''