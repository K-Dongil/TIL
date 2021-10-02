# '0' => '0000', '1' => '1001', 'A' => '1010', 'F' => '1111'
# 16진수를 10진수로 바꾸기
def hexToBinStr(hexV):
    # 1. 16진수를 10진수의 값으로 바꾼다
    if hexV.isdigit():
        numV = int(hexV)
    else:
        numV = ord(hexV) - ord('A') + 10
    
    # 2. 10진수의 값을 2진수로 바꾼다
    res = ''
    for j in range(3, -1, -1):
        if numV & 1 << j:
            res += '1'
        else:
            res += '0'
    return res

def binStrToDec(binStr):
    i = len(binStr)
    res = 0
    for s in binStr:
        res += int(s)*(2**i)
        i -= 1
    return res

lst = '0F97A3'
res = ''
for i in range(0, len(lst)):
    res += hexToBinStr(lst[i])

for pos in range(0, len(res)):
    org = res[pos:pos+4]
    print(binStrToDec(org))