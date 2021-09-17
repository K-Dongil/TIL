tc = int(input())

for t in range(tc):
	lst = input().split()
	n = len(lst) # 원소의 개수
	subset = [0]*(2**n)
	position = 0
	first = 0
	
	for i in range(1<<n): # i를 2진수로 표기한 값에는 arr의 어떤 원소들로 부분집합이 이루어져있는지 정보가 담겨있다
		b = 0
		a = 0
		for j in range(n): # j는 비트번호, 원소의 수만큼 비트를 비교
			if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력, #True or False
				b += int(lst[j])
				a += 1
		if a == 3:
			subset[i] = b
	
	subset = list(set(subset))

	subset.sort()
	print(f'#{t+1} {subset[-5]}')