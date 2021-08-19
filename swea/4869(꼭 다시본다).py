#f(n) = f(n-1) + 2*f(n-2)
#f(1) = 1, f(2) = 3
def f(n):
    if n==1:
        return 1
    if n==2:
        return 3
    return f(n-1) + 2*f(n-2)

TC = int(input())
for tc in range(1, TC+1):
    N = int(input()) // 10

    print('#{} {}'.format(tc, f(N)))
#
# # DP풀이
#
# TC = int(input())
#
# ARR = [0] * 31
# ARR[1] = 1`
# ARR[2] = 3
#
# for n in range(1, 31):
#     ARR[n] = ARR[n-1] + 2 * ARR[n-2]
#
# for tc in range(1, TC+1):
#     N = int(input()) // 10
#     print('#{} {}'.format(tc, ARR[N]))