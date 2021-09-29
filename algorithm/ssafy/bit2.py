def binStrToDec(binStr):
    i = len(binStr)
    res = 0
    for s in binStr:
        res += int(s)*(2**i)
        i -= 1
    return res

lst = '0000000111100000011000000111100110000110000111100111100111111001100111'

for pos in range(0, len(lst), 7):
    org = lst[pos:pos+7]
    print(binStrToDec(org))
