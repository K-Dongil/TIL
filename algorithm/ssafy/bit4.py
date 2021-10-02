def hexToBinStr(hexV):
    dict = {
        '0':'0000', '1':'0001', '2':'0010',
        '3':'0011', '4':'0100', '5':'0101',
        '6':'0110', '7':'0111', '8':'1000',
        '9':'1001', 'A':'1010', 'B':'1011',
        'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
    }
    return dict[hexV]

lst = '0DEC'
lst1 = '0269FAC9A0'
res = ''
for i in range(0, len(lst)):
    res += hexToBinStr(lst[i])

patt = ['001101', '010011', '111011', '110001',
        '100011', '110111', '001011', '111101',
        '011001', '101111']
pos = 0
while pos < len(res):
    if res[pos:pos+6] in patt:
        print(patt.index(res[pos:pos+6]))
        pos += 6
    else:
        pos += 1