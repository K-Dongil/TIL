import sys
sys.stdin = open("1240_input.txt", "r")

def codeToDecimal(binaryStr):
    global M
    codes = []
    sum = 0
    interpretation  = 0

    for i in range(len(binaryStr)-1, -1, -1):
        if binaryStr[i] == '1':
            for j in range(i-55, i+1, 7):
                codes.append(binaryStr[j:j+7])
            break
    
    for i in range(len(codes)):
        decimal = dict[codes[i]]
        if not (i+1) % 2:
            sum += decimal
        else:
            sum += decimal * 3
        interpretation += decimal
    
    if not sum % 10:
        return interpretation
    else:
        return '0'

dict ={
    '0001101':0, '0011001':1, '0010011':2,
    '0111101':3, '0100011':4, '0110001':5,
    '0101111':6, '0111011':7, '0110111':8, '0001011':9
}

tc = int(input())

for t in range(1, tc+1):
    N, M = map(int, input().split()) # 배열의 세로, 가로
    lst = [input() for _ in range(N)]
    result = 0

    for l in lst:
        if l.count('0') == M:
            continue
        a = codeToDecimal(l)
        if a:
            result = a
            break
    
    print(f'#{t} {result}')


# 이 문제는 암호코드를 앞에서부터 찾게 되면 틀린다.
# def binaryToDecimal(binaryStr):
#     global M
#     idx = 0
#     binary_code = ''
#     binarys = []
#     sum = 0
#     interpretation  = 0

#     while idx <= M-7:
#         if binaryStr[idx:idx+7] in dict:
#             binary_code = binaryStr[idx:idx+7]
#             binarys.append(binary_code)
#             idx += 7
#         else:
#             idx += 1
    
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
#         a = binaryToDecimal(l)
#         if a:
#             result = a
#             break
    
#     print(f'#{t} {result}')


# 교수님코드
# PATT = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

# TC = int(input())
# for tc in range(1, TC+1):
#     N, M = map(int, input().split())
#     ARR = [input() for _ in range(N)]

#     #1. 위에서부터 오른쪽 끝 지점을 찾는다
#     for row in range(N):
#         if '1' in ARR[row]:
#             col = ARR[row][::-1].index('1')
#             break
    
#     #2. 코드의 시작점을 계산한다
#     col = M - col -56

#     #3. 8개의 숫자를 찾는다.
#     res = []
#     for i in range(8):
#         res.append(PATT.index(ARR[row][col:col+7]))
#         col += 7
    
#     #4. res를 검증
#     oddS = res[0] + res[2] + res[4] + res[6]
#     evenS = res[1] + res[3] + res[5] + res[7]
#     if (oddS*3 + evenS) % 10 == 0:
#         print(oddS + evenS)