

# testcase : bananana nana
def typing(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    pattern_count = 0

    for idxT in range(str1_len - str2_len + 1):
        idxP = 0
        while idxP < str2_len and str1[idxT] == str2[idxT + idxP]:
            idxP += 1
            if idxP == 
            pattern_count += 1
            
            i += str2_len

    
    typing_count = str1_len - (pattern_count * str2_len) + pattern_count

    return typing_count

tc = int(input())

for t in range(tc):
    str1, str2 = input().split()

    print('#{} {}'.format(t+1, typing(str1, str2)))




# # 교수님 코드
# import sys
# sys.stdin = open("input_3143.txt","r")

# T = int(input())
# for tc in range(1, T+1):
#     str1, str2 = input().split()

#     n = len(str1)
#     m = len(str2)
#     cnt = 0
#     idxT = 0
#     while idxT < n-m+1:
#     #for idxT in range(n-m+1): #마지막위치 계산하는거 외우자
#         idxP = 0
#         while idxP < m and str1[idxT+idxP] == str2[idxP]:
#             idxP += 1
#         if idxP == m:
#             cnt += 1
#             idxT += idxP # m 도 가능
#         else: #패턴 못찾았을때
#             idxT += 1
#     cnt = cnt + n - (cnt*m)

#     print(f'#{tc} {cnt}')



# # 지원님 코드



# def check(str1, str2):
#     N = len(str1)
#     M = len(str2)   
#     i = 0
#     cnt = 0
    
#     while i < M - N + 1:

#         iscnt = 0
#         if str1[0] == str2[i]:
#             for j in range(len(str1)):
#                 if str1[j] == str2[i+j]:
#                     iscnt +=1 
#         if iscnt == N:
#             cnt += 1
#             i += N
#         else:
#             i += 1

#     return cnt

# T = int(input())

# for i in range(T):

#     str1, str2 = input().split()

#     N = len(str1)
#     M = len(str2)
#     num = check(str2, str1)

#     total_len = num + (N-M*num)


#     print(f'#{i+1} {total_len}')