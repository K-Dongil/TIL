import sys
sys.stdin = open('4864_input.txt', 'r')

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