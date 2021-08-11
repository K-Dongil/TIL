lst = [0, 1, 2, 3, 4]

N = 5
for i in range(1<<N): #0b11111 + 1 = 0b100000 = 1<<5 = 2^5
	#부분 집합 2^5개 중 하나인 i에 대한 sumV를 구한다.
	sumV = 0
	for j in range(N):
		r = i & (1<<j)
		if r != 0:
			sumV += lst[j]
	print(i, sumV)