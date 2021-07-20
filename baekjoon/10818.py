import sys
N = int(input())
L = list(map(int, sys.stdin.readline().split()))
min_num = min(L) #시퀀스형 데이터에서 가장 작은 값
max_num = max(L) #시퀀스형 데이터에서 가장 큰 값
print(min_num, max_num)
# import sys
# N = int(input())
# L = list(map(int, sys.stdin.readline().split())) #map함수는 결과값을 map형태로 반환하기 때문에 list로 형변환 필요
# for i in range(N):
#     for j in range(i+1, N):
#         if L[i] > L[j]:
#             max_num = L[i]
#             min_num = L[j]
#         elif L[i] < L[j]:
#             max_num = L[j]
#             min_num = L[i]
# print(min_num, max_num)