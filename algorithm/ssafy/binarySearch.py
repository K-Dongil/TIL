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




lst = [2, 4, 7, 9, 11, 19, 23]

def binaryS(key, lst): # key는 찾고자 하는 값
	start = 0
	end = len(lst) - 1
	while start <= end:
		m = (start+end)//2
		if key == lst[m]: # 검색성공
			return m
		elif key < lst [m]:
			end = m - 1 # 주의!!
		else:
			start = m +1 # 주의!!

	return -1

print(binaryS(7, lst)) # 2
print(binaryS(2, lst)) # 0
print(binaryS(23, lst)) # 6
print(binaryS(5, lst)) # -1
print(binaryS(1, lst)) # -1