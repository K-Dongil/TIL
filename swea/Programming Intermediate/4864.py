def brute_force(T, P):
    lenT = len(T)
    lenP = len(P)

    for i in range(lenT - lenP + 1):
        j = 0
        while j < lenP and P[j] == T[i+j]:
            j += 1
        if j == lenP:
            return 1
    return 0

t = int(input())

for tc in range(t):
    str1 = input()
    str2 = input()

    result = brute_force(str2, str1)
    print('#{} {}'.format(tc+1, result))

#========================================
tc = int(input())

for t in range(1, tc+1):
    str1 = input()
    str2 = input()
    result = 0

    if str1 in str2:
        result = 1
    
    print('#{} {}'.format(t, result))

#========================================
tc = int(input()) # brute force

for t in range(1, tc+1):
    str1 = input()
    str2 = input()
    result = 0

    for i in range(len(str2) - len(str1) + 1):
        for j in range(len(str1)):
            if str2[i+j] != str1[j]:
                result = 0
                break
            result = 1
        if result == 1:
            break

    print('#{} {}'.format(t, result))

#========================================
def brute(s1, s2):
    s1Len = len(s1)
    s2Len = len(s2)

    for i in range(s1Len - s2Len + 1):
        for j in range(s1Len):
            if str2[i+j] != str1[j]:
                break
            return 1
    return 0

tc = int(input())

for t in range(1, tc+1):
    str1 = input()
    str2 = input()

    result = brute(str1, str2)

    print('#{} {}'.format(t, result))