testcase = int(input()) # 테스트 케이스 갯수 입력 받음
for i in range(testcase): # 테스트 케이스 갯수만큼 for문을 돌릴 것임
    N = int(input()) # N은 2 이상 10,000,000 이하이다.
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while N != 1:
        if N % 2 ==0:
            a += 1
            N //= 2
        elif N % 3 ==0:
            b += 1
            N //= 3
        elif N % 5 ==0:
            c += 1
            N //= 5
        elif N % 7 ==0:
            d += 1
            N //= 7
        elif N % 11 ==0:
            e += 1
            N //= 11
    print(f'#{i+1} {a} {b} {c} {d} {e}')

#=================================================
# def divide(n, divisor, exponent):
#     if n % divisor == 0:
#         exponent += 1
#         n /= divisor
#     return n, exponent

# for i in range(test_case):
#     number = int(input())

#     a, b, c, d, e = 0, 0, 0, 0, 0

#     while number != 1:
#         number, a = divide