# 시간이 너무 오래걸린다
import sys

sys.stdin = open('1216_input.txt', 'r')

tc = 10

for t in range(tc):
    tc_num = int(input())

    str_lst = [input() for _ in range(100)]
    best_circle = 0

    for i in range(100):
        add_str = ''
        for j in range(100):
            add_str += str_lst[j][i]
        str_lst.append(add_str)

    for i in range(100, 1, -1):
        new_str_lst = []
        for j in str_lst:
            for k in range(len(j) - i + 1):
                new_str_lst.append(j[k:k + i])
        for s in new_str_lst:
            new_str = ''
            for j in range(len(s) - 1, -1, -1):
                new_str += s[j]
            if s == new_str and len(s) == i:
                best_circle = len(s)
                break
        if best_circle == i:
            print('#{} {}'.format(tc_num, best_circle))
            break