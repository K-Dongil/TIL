T = int(input()) # 테스트 케이스 개수 입력 받음
for i in range(T): # 테스트 케이스 갯수만큼 for문 돌림
    a = 0 # 몇번 째 인지 알려주는 변수
    N = int(input()) # 배수 입력받는다
    lst = [] # 0~9까지의 숫자가 넣어질 리스트
    while len(lst) <10: # 리스트의 길이가 10이상일 때 while문 멈출 것임
        a += 1 # 몇번 째 인지 세기위해 while문 돌아갈 때 마다 1씩 증가
        for j in str(N * a): # N*a번 째에서 볼 수 있는 숫자들을 임시변수 i에 담아 for문 돌린다 (그러기 위하여 N*a를 str형변환)
            if j not in lst: # 만약 리스트에 N*a번째에서 볼 수 있는 숫자가 담겨져 있지 않다면
                lst.append(j) # 리스트에 N*a번째에서 볼 수 있는 숫자 추가
    print(f'#{i+1} {a*N}') # 몇 번째의 양인지 출력