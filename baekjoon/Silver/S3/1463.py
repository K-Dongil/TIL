num = int(input())
dp = [0]*(num+1)

for i in range(2, num+1):
    dp[i] = dp[i-1] + 1 # 이전 값에서 +1한 값이 최저 횟수일 수 있으니깐

    if i%2 == 0: # 2 또는 3으로 나누어질 때는 어떠한 방법이 더 적은 횟수로 만들 수 있는지 확인
        dp[i] = dp[i] if dp[i] < dp[i//2]+1 else dp[i//2]+1
    if i%3 == 0:
        dp[i] = dp[i] if dp[i] < dp[i//3]+1 else dp[i//3]+1

print(dp[num])