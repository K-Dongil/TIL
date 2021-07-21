#피보나치
#재귀
def fibonacci(n):
    #base case가 필요
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4)) # 1 1 2 3

#반복
def fibo(n):
    if n < 2:
        return n
    a, b =0, 1

    for i in range(n-1):
        a, b = b, a+b
    return b
print(fibo(4))