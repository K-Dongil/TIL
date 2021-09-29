# 10진수의 값을 2진수로 표현하기
# 10 => 00001010 (8bit)
def dectobinstr(num):
    res = ''
    for j in range(7, -1, -1):
        if num & (1<<j):
            res += '1'
        else:
            res += '0'
    return res

print(dectobinstr(10))