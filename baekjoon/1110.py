a =0 # 횟수 저장할 변수
N = int(input()) #입력받을 변수
n = N #입력받은 값을 기억할 변수
while True:
    N = ((N%10)*10) + ((N//10 + N%10)%10)
    a += 1 # count
    if N == n: #변하는 값이 초기값과 같아지면
        print(a) #횟수 출력
        break #멈춘다