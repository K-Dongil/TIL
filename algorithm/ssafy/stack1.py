s1 = '( )( )((( )))'
#s1 = '(( )'
# s1 = '( ))'

ST = []
result = 'OK'
for c in s1:
    if c=='(':
        ST.append(c)
    if c==')':
        if len(ST) == 0:
            result = 'ERR'
            break

        ST.pop(-1)

if len(ST) > 0:
    result = 'ERR'

print(result)