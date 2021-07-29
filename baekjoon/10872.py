def factorial(n): # 팩토리얼 재귀함수
    if n <= 1: # 매개변수가 n 이하일 때
        return 1 # 재귀를 멈춤
    return n * factorial(n-1) # 매개변수 n * n-1 * n-2 ....................
N = int(input()) # 숫자 입력받음
print(factorial(N)) # 반환값 출력

# 밑에 코드가 시간이 더 걸린다.
# N = int(input())
# def factorial(n):
#     if n > 1:
#         return n * factorial(n-1)
#     return 1
# print(factorial(N))