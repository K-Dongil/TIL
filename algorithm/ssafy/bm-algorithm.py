T = 'rithm Process finished with exit code 0'

def BM(P):
    M = len(P)
    N = len(T)

    SKIP = [M] * 128
    for i in range(M):
        # pos = ord(P[i])
        # SKIP[pos] = M-i-1
        SKIP[ord(P[i])] = M - i - 1
    idxT = 0 # 시작 위치
    while idxT < N-M:
        idxP = M - 1 # 끝위치
        while idxP >= 0 and T[idxT + idxP] == P[idxP]:
            idxP -= 1
        if idxP == -1: # 찾았다면
            return idxT
        #pos = ord(T[idxT+M-1])
        idxT = idxT + SKIP[ord(T[idxT+M-1])]

    return -1

print(BM('rithm'))

# def pattern_BMOOR(T, P):
#     lenT = len(T)
#     lenP = len(P)
#
#     jumpA = [lenP] * 128
#     value = 0
#     for i in range(lenP-1, -1, -1):
#         c = P[i]
#         jumpA[ord(P[i])] = value
#         value += 1
#
#
#     while idxT <
#         idxP = 마지막위치
#         # lastT =
#         역으로 비교
#
#         while idxP < lenP and P[idxP] == T[]:
#             idxP += 1
#         if idxP == lenP:  #
#             return idxT
#         else:
#             jump
#
#     return -1
#
# T = "TTTTAACCABCDETTATTTF"
# P = "TTATTT"
#
#
# result = pattern_B(T, P)
# print(result)