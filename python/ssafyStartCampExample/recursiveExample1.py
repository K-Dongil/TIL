#팩토리얼
#반복
def fact(n):
    result = 1 # 팩토리얼은 곱하는거니깐 1로 초기화
    while n > 1:
        result *= n
        n -= 1
    return result
# print(fact(3)) # 6
# print(fact(4)) # 24

#재귀
def factorial(n):
    if n ==1 :
        return n
    else:
        return n * factorial(n-1)
print(factorial(4)) # 24