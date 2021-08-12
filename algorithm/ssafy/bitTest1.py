lst = [0, 1, 2, 3, 4] # 원소가 5개, 부분집합의 개수 : 2^5개
N = 5
for i in range(1<<N): #0b11111 + 1 = 0b100000 = 1<<5 = 2^5
	#부분 집합 2^5개 중 하나인 i에 대한 sumV를 구한다.
	sumV = 0
	for j in range(N): # 집합의 원소의 개수
		r = i & (1<<j) # 0 ~ N-1 번째 자리의 bit가 0인지 1인지 판단하기 위함
		if r != 0: # 만약 j번째 자리의 bit가 1이라면(= 집합에서의 j번째 요소가 i부분집합에 포함 )
			sumV += lst[j] # 부분집합의 합을 나타내는 sumV 변수에 리스트의 ?번째 데이터 값을 더한다
	print(i, sumV)