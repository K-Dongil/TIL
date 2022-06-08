import sys

sys.stdin = open("1240_input.txt", "r")


def binaryToDecimal(binaryStr):
    global M
    idx = 0
    binary_code = ''
    binarys = []
    decimals = []
    sum = 0
    decimal_code = '0'

    while idx <= M - 7:
        if binaryStr[idx:idx + 7] in dict:
            binary_code = binaryStr[idx:idx + 7]
            binarys.append(binary_code)
            idx += 7
        else:
            idx += 1

    for binary in binarys:
        decimal = binStrToDec(binary)
        sum += decimal
        decimals.append(decimal)

    if not sum // 10:
        decimal_code = ''.join(decimals)

    return decimal_code


def binStrToDec(binStr):
    i = len(binStr)
    res = 0
    for s in binStr:
        res += int(s) * (2 ** i)
        i -= 1
    return res


dict = {
    '0001101': '0', '0011001': '1', '0010011': '2',
    '0111101': '3', '0100011': '4', '0110001': '5',
    '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'
}

tc = int(input())

for t in range(1, tc + 1):
    N, M = map(int, input().split())  # 배열의 세로, 가로
    lst = [input() for _ in range(N)]
    result = 0

    for l in lst:
        if l.count('0') == M:
            continue
        a = binaryToDecimal(l)
        if a:
            result = a
            break

    print(f'#{t + 1} {result}')