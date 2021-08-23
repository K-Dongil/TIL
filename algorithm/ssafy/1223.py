for tc in range(10):
    s_len = int(input())
    s = input()
    ST = ['Check']
    lst = []
    for c in s:
        if c.isdecimal():
            lst.append(c)
        elif c == '+':
            if ST[-1] == '*':
                while ST[-1] == '*':
                    lst.append(ST.pop(-1))
            ST.append(c)
        else:
            ST.append(c)
    while ST:
        lst.append(ST.pop(-1))  # 6번

    i = 0
    while len(lst) != 2:
        if lst[i] == '*':
            a = lst[i]
            b = lst[i - 1]
            c = lst[i - 2]
            lst.pop(i)
            lst.pop(i - 1)
            lst[i - 2] = int(c) * int(b)
            i -= 2
        elif lst[i] == '+':
            a = lst[i]
            b = lst[i - 1]
            c = lst[i - 2]
            lst.pop(i)
            lst.pop(i - 1)
            lst[i - 2] = int(c) + int(b)
            i -= 2
        i += 1
    print('#{} {}'.format(tc+1, lst[0]))
