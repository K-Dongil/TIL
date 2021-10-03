def dectobinstr(num1, num2):
    res = ''
    for j in range(num2-1, -1, -1):
        if num1 & (1<<j):
            res += '1'
        else:
            res += '0'
    return res

tc = int(input())

for t in range(1, tc+1):
    N, M = map(int, input().split())
    result = 'ON'
    binstr = dectobinstr(M, N)
    
    if binstr.count('0'):
        result = 'OFF'
    
    print(f'#{t} {result}')


# ============================================
# def dectobinstr(num1, num2):
#     global result
#     res = ''
#     for j in range(num2-1, -1, -1):
#         if num1 & (1<<j):
#             res += '1'
#         else:
#             result = 'OFF'
#             break
#     return res

# tc = int(input())

# for t in range(1, tc+1):
#     N, M = map(int, input().split())
#     result = 'ON'
#     binstr = dectobinstr(M, N)
    
#     print(f'#{t} {result}')