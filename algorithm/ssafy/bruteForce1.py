def pattern_B(T, P):
    lenT = len(T)
    lenP = len(P)

    for idxT in range(lenT - lenP):
        idxP = 0
        while idxP < lenP and P[idxP] == T[]:
            idxP += 1
        if idxP == lenP:  #
            return idxT
        else:
            idxT += 1
    return -1

T = "TTTTAACCABCDETTATTTF"
P = "TTATTT"


result = pattern_B(T, P)
print(result)



def pattern_BMOOR(T, P):
    lenT = len(T)
    lenP = len(P)
s
    jumpA = [lenP] * 128
    value = 0
    for i in range(lenP-1, -1, -1):
        c = P[i]
        jumpA[ord(P[i])] = value
        value += 1


    while idxT <
        idxP = 마지막위치
        # lastT =
        역으로 비교

        while idxP < lenP and P[idxP] == T[]:
            idxP += 1
        if idxP == lenP:  #
            return idxT
        else:
            jump

    return -1

T = "TTTTAACCABCDETTATTTF"
P = "TTATTT"


result = pattern_B(T, P)
print(result)