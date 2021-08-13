def itoa(value): # 정수를 문자열로 바꿔 주는 것
    t = []

    if value < 0:
        isMinus = True
        value *= -1
    else:
        isMinus = False

    while value > 0:
        tt =value % 10
        t.append(chr(tt + 0x30))
        value = value // 10

    t.reverse()
    if isMinus:
        return '-' + ''.join(t)

    return  ''.join(t)




print(itoa(123), type(itoa(123)))
print(itoa(-123), type(itoa(-123)))