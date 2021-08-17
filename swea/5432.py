# testcase : bananana nana
def typing(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    pattern_count = 0

    for i in range(str1_len - str2_len + 1):
        print(i)
        if str1[i:i+str2_len] == str2:
            pattern_count += 1
            
            i += str2_len

    
    typing_count = str1_len - (pattern_count * str2_len) + pattern_count

    return typing_count

tc = int(input())

for t in range(tc):
    str1, str2 = input().split()

    print('#{} {}'.format(t+1, typing(str1, str2)))




# # 교수님 코드
# N = len(T)
# M = len(P)

# while idxT < N-M+1:
#     idxP = 0
#     while idxP < M and T[idxT] == P[idxP]:
#         ???
#     if idx == M:
#         cnt += 1


TC = int(input())

for tc in range(TC):
    str1, str2 = input().split()

    N = len(str1)
    M = len(str2)
    cnt = 0
    for idxT in range(N-M+1):
        idxP = 0
        while idxP < M and str1[idxT] == str2[idxP]:
            idxP += 1
            if idxP == M:
                cnt += 1
                idxT += M
            else:
                idxT += 1

    print('#{} {}'.format(tc + 1, typing(str1, str2)))