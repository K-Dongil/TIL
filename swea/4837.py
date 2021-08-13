A = list(range(1, 13)) # 원소가 12개, 부분집합의 개수 : 2^12개
t = int(input()) # 테스트 케이스 수 입력 받음

for i in range(t): # 테스트 케이스 개수만큼 반복
    subset_element, subset_sum = map(int, input().split()) # 집합의 원소의 몇개로 부분집합이 이루어졌는지, 부분집합의 합은 몇인지 입력받는다
    want_subset = 0 # 위의 조건을 만족하는 부분집합을 counting할 변수
    
    for j in range(1<<12): # #0b111111111111 + 1 = 0b1000000000000 = 1<<12 = 2^12,  부분집합의 개수는 2^12개
        element_count = 0 # 현재 부분집합의 원소가 몇개 있는지 couning할 변수
        element_sum = 0 # 현재 부분집합의 합을 저장해둘 변수
        for k in range(12): # 집합의 원소가 12개 이므로
            if j & (1<<k): # j의 bit는 j번째 부분집합이 어떻게 생겼는지 나타낸다. 각 자리의 bit가 0인지 1인지 check하여 부분집합의 원소를 알아낸다
                element_sum += A[k] # k번째 bit가 1이라면 집합에서 k번째 원소는 j번째 부분집합의 원소
                element_count += 1 # 부분집합의 원소를 세주는 변수에 +1을 해준다
        if element_count == subset_element and element_sum == subset_sum: # 만약 부분집합의 원소의 개수와 합이 입력받은 값과 같다면
            want_subset += 1 # 구하고자 하는 부분집합이 1개 늘어난 것

    print('#{} {}'.format(i+1, want_subset)) # 테스트케이스와 조건을 만족하는 부분집합의 개수를 출력


# # 교수님 풀이
# import sys
# sys.stdin = open("input", "r")
# TC = int(input().split())
# for tc in range(1, TC+1):
#     N, K = map(int, input())
#     lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#     BITS = 12 #0b000000000000 ~ 0b111111111111
#     for i in range(1<<12): # 0b111111111111 + 1 == 1<<12
#         sumV = 0
#         cnt = 0
#         for j in range(BITS):
#             if i & (1<<j): # j번째 bit가 0인지 1인지 check
#                 sumV += lst[j]
#                 cnt += 1