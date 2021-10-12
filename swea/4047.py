# 스페이드, 다이아몬드, 하트, 클로버 : S, D, H, C
tc = int(input())

for t in range(tc):
    card_str = input()
    S = [0] * 14
    D = [0] * 14
    H = [0] * 14
    C = [0] * 14
    result = ''

    for i in range(0, len(card_str),3):
        num = 0
        if card_str[i] == 'S':
            num = int(card_str[i+1]+card_str[i+2])
            if not S[num]:
                S[num] = 1
            else:
                result = 'ERROR'
                break
        elif card_str[i] == 'D':
            num = int(card_str[i+1]+card_str[i+2])
            if not D[num]:
                D[num] = 1
            else:
                result = 'ERROR'
                break
        elif card_str[i] == 'H':
            num = int(card_str[i+1]+card_str[i+2])
            if not H[num]:
                H[num] = 1
            else:
                result = 'ERROR'
                break
        elif card_str[i] == 'C':
            num = int(card_str[i+1]+card_str[i+2])
            if not C[num]:
                C[num] = 1
            else:
                result = 'ERROR'
                break
    else:
        result += str(S.count(0) -1) + " "
        result += str(D.count(0) -1) + " "
        result += str(H.count(0) -1) + " "
        result += str(C.count(0) -1) + " "
    print(f'#{t+1} {result}')