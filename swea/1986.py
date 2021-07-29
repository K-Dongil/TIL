T = int(input())
for i in range(T):
    N = int(input())
    total = 0
    for j in range(1, N+1):
        if j % 2:
            total += j
        else:
            total -= j
    print(f'#{i+1} {total}')

#==================================================================================================
def sumNum(num): # 매개변수 num
    plusNum = 0 # 홀수는 더하고 짝수는 빼주는 값을 저장해줄 변수
    for i in range(1, num+1): # 1 ~ 입력받은 매개변수 num까지 for문을 돌린다
        if i % 2: # 만약 홀수번째의 값이라면
            plusNum += i # 더해준다
        else: # 만약 짝수번째의 값이라면
            plusNum -= i # 빼준다
    return plusNum # 최종값을 반환

testcase = int(input()) # 테스트케이스 갯수 입력받음
for i in range(testcase): # 갯수만큼 for문을 반복
    number  = int(input()) # 숫자를 입력받음
    plusNum = sumNum(number) # 입력받은 숫자를 1~number까지 홀수는 더하고 짝수는 빼주는 함수에 인자로 넣어준다
    print(f'#{i+1} {plusNum}') # i번째 테스트케이스, 더하고 뺀 값의 최종값 출력

#==================================================================================
cnt = int(input())

for i in range(cnt):
    n = int(input())

    if n%2 ==1:
        k = -1 * (n//2) + n
    else:
        k = -1 * (n//2)
    print(f'#{i+1} {k}')