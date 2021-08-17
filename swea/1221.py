t = int(input())

for tc in range(t):
    tc_num, tc_len = input().split()

    str_lst = input().split()
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    for s in str_lst:
        if s == 'ZRO':
            zero += 1
        elif s == 'ONE':
            one += 1
        elif s == 'TWO':
            two += 1
        elif s == 'THR':
            three += 1
        elif s == 'FOR':
            four += 1
        elif s == 'FIV':
            five += 1
        elif s == 'SIX':
            six += 1
        elif s == 'SVN':
            seven += 1
        elif s == 'EGT':
            eight += 1
        else:
            nine += 1
    statistics =[zero, one, two, three, four, five, six, seven, eight, nine]
    sort_str_lst = ['ZRO '*zero, 'ONE '*one, 'TWO '*two, 'THR '*three, 'FOR '*four, 'FIV '*five, 'SIX '*six, 'SVN '*seven, 'EGT '*eight, 'NIN '*nine]
    print(tc_num)
    print(* sort_str_lst)


# t = int(input())

# for tc in range(t):
#     tc_num, tc_len = input().split()

#     str_lst = input().split()
#     str_set = list(set(str_lst))
   
#     sum_lst = [0]*10

#     for i in range(len()):
#     for s in str_lst:
#         if s == 'ZRO':
#             sum_lst[0] += 1
#         elif s == 'ONE':
#             sum_lst[1] += 1
#         elif s == 'TWO':
#             sum_lst[2] += 1
#         elif s == 'THR':
#             sum_lst[3] += 1
#         elif s == 'FOR':
#             sum_lst[4] += 1
#         elif s == 'FIV':
#             sum_lst[5] += 1
#         elif s == 'SIX':
#             sum_lst[6] += 1
#         elif s == 'SVN':
#             sum_lst[7] += 1
#         elif s == 'EGT':
#             sum_lst[8] += 1
#         else:
#             sum_lst[9] += 1

#     sort_str_lst = ['ZRO '*sum_lst[0], 'ONE '*sum_lst[1], 'TWO '*sum_lst[2], 'THR '*sum_lst[3], 'FOR '*sum_lst[4], 'FIV '*sum_lst[5], 'SIX '*sum_lst[6], 'SVN '*sum_lst[7], 'EGT '*sum_lst[8], 'NIN '*sum_lst[9]]
#     print(tc_num)
#     print(* sort_str_lst)



# T = int(input())
# for test_case in range(1, T+1):
#     N = input()
#     dict_str = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
#     lst_str = input().split()
#     result = ''
#     for s in lst_str:
#         dict_str[s] += 1
 
#     for key, value in dict_str.items():
#         temp = ' '.join([key] * value)
#         result += temp +' '
#     print(f'#{test_case}',end=' ')
#     print(result[:len(result)-1])



# # 교수님 코드
# import sys
# sys.stdin = open("input1221.txt", "r")

# TC = int(input())
# pattern = ['ZRO ', 'ONE ', 'TWO ', 'THR ', 'FOR ', 'FIV ', 'SIX ', 'SVN ', 'EGT ', 'NIN ']

# for tc in range(1, TC+1):
#     No = input()
#     lst = list(input().split())

#     for p in pattern:
#         #lst에서 p랑 같은 것을 출력해라
#         for s in lst:
#             if p==s:
#                 print(s, end=' ')

#     print()