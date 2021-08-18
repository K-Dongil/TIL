def fibo(n):
	global cnt
	cnt += 1
	if n>=2 and memo[n]==0: # 아직 계산되지 않은 값이면
		memo[n] = fibo(n-1) + fibo(n-2)
	return memo[n]

def fibo1(n):
	if n>=2 and len(memo1)<=n:
		memo1.append(fibo1(n-1) + fibo1(n-2))
	return memo1[n]



n = 50
memo = [0] * (n+1) # n값 자체를 index로 쓰기위하여 n+1
memo[0] = 0
memo[1] = 1
cnt = 0
print(fibo(n), cnt)


memo1 = [0,1]
print(fibo1(n))