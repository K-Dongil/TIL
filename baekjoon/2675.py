T = int(input()) # 테스트 케이스 개수
for i in range(T): # 테스트 케이스 개수만큼 for문 돌리기
    A, B = input().split() # 공백을 기준으로 입력받은 값 구분하여 str형태로 입력받음
    for i in B: # 문자열에 있는 한개의 문자마다 i에 담아서 for문 돌림
        print(i*int(A), end='') # 문자를 int형으로 바꾼 A만큼 반복 출력하고 줄바꿈X
    else: # for문 끝나면
        print() # 줄바꿈