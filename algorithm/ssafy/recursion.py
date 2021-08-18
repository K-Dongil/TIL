def f(i, k):
	if i==k: # 배열을 벗어나면(모든 원소에 대한 작업이 끝나면)
		return
	else:
		print(A[i])
		f(i+1, k) # 다음 원소로 이동
N = 3
A = [10, 20, 30]
f(0, N) # 배열을 출력하는 함수