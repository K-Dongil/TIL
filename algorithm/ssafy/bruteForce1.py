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