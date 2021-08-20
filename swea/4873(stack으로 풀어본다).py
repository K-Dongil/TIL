def overlap_remove(str):
    break_condition = 0
    str_lst = []
    for s in str:
        str_lst.append(s)
        
    while break_condition == 0:
        if len(str_lst) == 2:
            if str_lst[0] == str_lst[1]:
                return 0
        elif len(str_lst) == 1:
            return 1

        for i in range(len(str_lst)-1):
            if str_lst[i] == str_lst[i+1]:
                str_lst.pop(i+1)
                str_lst.pop(i)
                break
            if i == len(str_lst)-2:
                break_condition = 1

    return len(str_lst)

tc = int(input())

for t in range(tc):
    str = input()
    print('#{} {}'.format(t+1, overlap_remove(str)))


# # 다른 코드
# t = int(input())
# for num in range(1, t + 1):
#     arr = list(map(str, input()))
#     result = []
#
#     for i in range(len(arr)):
#         if len(result) == 0:
#             result.append(arr[i])
#         elif arr[i] != result[-1]:
#             result.append(arr[i])
#         else:
#             result.pop(-1)
#     print(f'#{num} {(len(result))}')