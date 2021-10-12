# # 코드 끝이 전부 1 : 1, 3, 5, 7, 9, B, D, F 중 한개
# import sys
# sys.stdin = open("1242_input.txt", "r")
# def hexToBinStr(hexV):
#     hexaToBindict = {
#         '0':'0000', '1':'0001', '2':'0010',
#         '3':'0011', '4':'0100', '5':'0101',
#         '6':'0110', '7':'0111', '8':'1000',
#         '9':'1001', 'A':'1010', 'B':'1011',
#         'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
#     }
#     return hexaToBindict[hexV]


# def binaryToDecimal(binaryStr):
#     global M
#     idx = 0
#     binary_code = ''
#     binarys = []
#     sum = 0
#     interpretation  = 0

#     for i in range(len(binaryStr)-1, -1, -1):
#         if binaryStr[i] == '1':
#             for j in range(i-55, i+1, 7):
#                 binarys.append(binaryStr[j:j+7])
#             break
    
#     for i in range(len(binarys)):
#         decimal = dict[binarys[i]]
#         if not (i+1) % 2:
#             sum += decimal
#         else:
#             sum += decimal * 3
#         interpretation += decimal
    
#     if not sum % 10:
#         return interpretation
#     else:
#         return '0'

# dict ={
#     '0001101':0, '0011001':1, '0010011':2,
#     '0111101':3, '0100011':4, '0110001':5,
#     '0101111':6, '0111011':7, '0110111':8, '0001011':9
# }

# tc = int(input())

# for t in range(1, tc+1):
#     N, M = map(int, input().split()) # 배열의 세로, 가로
#     lst = [input() for _ in range(N)]
#     result = 0

#     for l in lst:
#         if l.count('0') == M:
#             continue
#         binstr = ''
#         for s in l:
#             binstr += hexToBinStr(s)
#         print(binstr)
#         # a = binaryToDecimal(binstr)
#         # if a:
#         #     result = a
#         #     break
    
#     print(f'#{t} {result}')


# 교수님코드
def hexToBinStr(hexV):
    hexaToBindict = {
        '0':'0000', '1':'0001', '2':'0010',
        '3':'0011', '4':'0100', '5':'0101',
        '6':'0110', '7':'0111', '8':'1000',
        '9':'1001', 'A':'1010', 'B':'1011',
        'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
    }
    return hexaToBindict[hexV]

PATT = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

PATT = [211, 221, 122, 411, 132, 231, 114, 312, 213, 112]

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    ARR = [input() for _ in range(N)]

    for i in range(N):
        ARR[i] = hexToBinStr(ARR[i][0:M])

    sumV = 0
    #1. 위에서부터 오른쪽 끝 지점을 찾는다 -> 여러개 찾는 경로
    for row in range(1, N):
        if ARR[row].find('1') < 0:
            continue


        col = M*4 -1
        while col > 56:
            if ARR[row][col] == '1' and ARR[row-1][col] == '0':
                res = []
                for i in range(8):
                    cnt1 = cnt2 = cnt3 = 0
                    while ARR[row][col] == '1':
                        cnt1 += 1
                        col -= 1
                    while ARR[row][col] == '0':
                        cnt2 += 1
                        col -= 1
                    while ARR[row][col] == '1':
                        cnt3 += 1
                        col -= 1

                    while col>=0 and  ARR[row][col] == '0':
                        col-= 1

                    r = min(cnt1, cnt2, cnt3)
                    tnum = PATT.index(cnt3//r * 100 + cnt2//r*10 + cnt1//r)
                    res.insert(0, tnum)

                oddV = res[0] + res[2] + res[4] + res[6]
                evenV = res[1] + res[3] + res[5] + res[7]

                if (oddV*3 + evenV) % 10 == 0:
                    sumV += sum(res)
        else:
            col -= 1
    print(sumV)