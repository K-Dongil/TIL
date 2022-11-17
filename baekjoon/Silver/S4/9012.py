tc = int(input())

for t in range(tc):
    parenthesisStr = input()
    st = []
    result = 'YES'

    for s in parenthesisStr:
        if s == '(':
            st.append(s)
        else:
            if len(st):
                lastV = st.pop()
                if lastV == ')':
                    result = 'NO'
                    break
            else:
                result = 'NO'
                break
    
    if result == 'YES' and len(st):
        result = 'NO'
    
    print(result)