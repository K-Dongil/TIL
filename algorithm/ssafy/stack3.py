#계산기

# def step1(s):
#     postfix = []
#     ST = []
#     for c in s:
#         if c.isdecimal():
#             postfix.append(c)
#         else:
#             if c == '(':
#                 ST.append(c)
#             elif c == ')':
#                 while ST and ST[-1] != '(':
#                     postfix.append(ST.pop(-1))
#             elif c in ['+', '-']:
#                 while ST and  ST[-1] in ['*', '/']:
#                     postfix.append(ST.pop(-1))
#                 ST.append(c)
#             elif c in ['*', '/']:
#                 while ST and  ST[-1] in ['*', '/']:
#                     postfix.append(ST.pop(-1))
#                 ST.append(c)
#
#     while ST:
#         if ST[-1] == '(':
#             ST.pop(-1)
#         else:
#             postfix.append(ST.pop(-1))
#
#     return postfix

def step1(s):
    isp = {'(':0, '+':1, '-':1, '*':2, '/':2}
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
    postfix = []
    ST = []
    for c in s:
        if c.isdecimal():
            postfix.append(c)
        else:
            if c == ')':
                while ST and ST[-1] != '(':
                    postfix.append(ST.pop(-1))
            elif len(ST)==0 or (ST and isp[ST[-1]] < icp[c]):
                ST.append(c)
            else:
                while ST and isp[ST[-1]] >= icp[c]:
                    postfix.append(ST.pop(-1))
                ST.append(c)

    while ST:
        if ST[-1] == '(':
            ST.pop(-1)
        else:
            postfix.append(ST.pop(-1))

    return postfix

def step2(t):
    ST = []
    for c in t:
        if c.isdecimal():
            ST.append(c)
        else:
            n1 = int(ST.pop())
            n2 = int(ST.pop())
            if c == '+':
                ST.append(n2+n1)
            elif c == '-':
                ST.append(n2-n1)
            elif c == '*':
                ST.append(n2*n1)
            elif c == '/':
                ST.append(n2/n1)
    return ST[0]

s = '2+((2*5)/5)'
s = step1(s)
print(s)
print(step2(s))