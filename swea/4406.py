tc = int(input())

for t in range(tc):
    str = input()
    str_lst = []
    for s in str:
        if s not in ['a', 'e', 'i', 'o', 'u']:
            str_lst.append(s)
    str_lst = ''.join(str_lst)
    print('#{} {}'.format(t+1, str_lst))