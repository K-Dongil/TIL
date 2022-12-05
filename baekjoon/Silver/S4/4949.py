parentheses = {
    '(' : ')',
    '[' : ']'
}

while True:
    inputStr = input()
    st = []
    result = 'yes'

    if inputStr == '.':
        break

    for s in inputStr:
        if s in ['(', '[']:
            st.append(s)
        elif s in [')', ']']:
            if len(st):
                lastV = st.pop()
                if parentheses[lastV] != s:
                    result = 'no'
                    break
            else:
                result = 'no'
                break
    else:
        if len(st):
            result = 'no'
    
    print(result)