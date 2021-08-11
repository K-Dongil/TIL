def binarySearch(a, key):
	start = 0
	end = len(a) -1 # type : int
	while start <= end:
		middle = (start + end)//2
		if a[middle] == key: # 검색성공
			return middle
		elif a[middle] > key:
			end = middle -1   # 주의해야할 곳!!
		else:
			start = middle + 1  # 주의해야할 곳!!
	return -1 # 검색 실패

arr = [2, 4, 7, 9, 11, 19, 23]
print(binarySearch(arr, 11))
print(binarySearch(arr, 10))