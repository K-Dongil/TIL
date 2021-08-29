def Forth(lst):
    ST = []
    for l in lst:
        if l.isdecimal(): # isdecimal은 문자열안에 값이 숫자로만 이루어져있는지 판단
            ST.append(l)
        elif l == '.':
            if 1 < len(ST):
                return 'error'
            return ST[0]
        else:
            if len(ST) < 2:
                return 'error'
            n1 = int(ST.pop())
            n2 = int(ST.pop())
            if l == '+':
                ST.append(n2+n1)
            elif l == '-':
                ST.append(n2-n1)
            elif l == '*':
                ST.append(n2*n1)
            elif l == '/':
                ST.append(n2//n1)

tc = int(input())

for t in range(tc):
    str_lst = input().split()
    result = Forth(str_lst)
    print('#{} {}'.format(t+1, result))

# 3 3 3 + .