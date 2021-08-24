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
                ST.pop(-1) # 이부분을 안 해줄시
            elif c == '(' or (ST and isp[ST[-1]] < icp[c]):
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

for tc in range(10):
    s_len = int(input())
    s = input()
    postfix_s = step1(s)
    result = step2(postfix_s)

    print('#{} {}'.format(tc+1, result))



# for tc in range(10):
#     s_len = int(input())
#     s = input()
#     ST = ['Check']
#     lst = []
#     for c in s:
#         if c.isdecimal():
#             lst.append(c)
#         elif c == '+':
#             if ST[-1] == '*':
#                 while ST[-1] == '*':
#                     lst.append(ST.pop(-1))
#             ST.append(c)
#         else:
#             ST.append(c)
#     while ST:
#         lst.append(ST.pop(-1))  # 6번
#
#     i = 0
#     while len(lst) != 2:
#         if lst[i] == '*':
#             a = lst[i]
#             b = lst[i - 1]
#             c = lst[i - 2]
#             lst.pop(i)
#             lst.pop(i - 1)
#             lst[i - 2] = int(c) * int(b)
#             i -= 2
#         elif lst[i] == '+':
#             a = lst[i]
#             b = lst[i - 1]
#             c = lst[i - 2]
#             lst.pop(i)
#             lst.pop(i - 1)
#             lst[i - 2] = int(c) + int(b)
#             i -= 2
#         i += 1
#     print('#{} {}'.format(tc+1, lst[0]))
