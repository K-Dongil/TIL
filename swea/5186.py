def decimalToBinary(f_num):
    num = 0
    i = -1
    res = ''
    while num != f_num:
        if f_num - num >= 2**(i):
            num += 2**(i)
            res += '1'
        else:
            res += '0'
        i -= 1
    if 13 <= len(res):
        res = 'overflow'
    
    return res

tc = int(input())

for t in range(1, tc+1):
    N = float(input())

    print(f'#{t} {decimalToBinary(N)}')



# 교수님 풀이
# TC = int(input())
# for tc in range(1, TC+1):
#     N = float(input())
#     C = 1

#     res = ''
#     found = False
#     for i in range(12):
#         C *= 0.5

#         if N == 0:
#             found = True
#             break
#         if N >= C:
#             N = N - C
#             res += '1'
#         else:
#             res += '0'

#     if found:
#         print(res)
#     else:
#         print('overflow') 

