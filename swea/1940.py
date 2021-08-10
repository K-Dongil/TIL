T = int(input()) # 테스트 케이스 입력 받음

for i in range(T): # 테스트 케이스만큼 반복
    move = 0 # 움직인 거리를 저장해놓을 공간
    velocity =0 # 속력을 저장해놓을 공간
    command_lst = [] # 커맨드 입력받은 것을 리스트에 저장
    N = int(input()) # 커맨드 입력을 몇 번 받을건지 임력받음
    
    for j in range(N): # N번만큼 반복    
        command_lst.append(list(map(int, input().split()))) # 입력받은 커맨드들을 리스트에 추가

    for k in range(len(command_lst)): # 입력받은 커맨드 횟수만큼 for문 반복
        # if command_lst[k][0] == 0: # 만약 입력받은 커맨드가 0이라면
        #     pass
        if command_lst[k][0] == 1: # 만약 입력받은 커맨드가 1이라면
            velocity += command_lst[k][1] # 가속도가 있으므로 속력에 가속도를 더해준다
        elif command_lst[k][0] == 2: # 만약 입력받은 커맨드가 2인데
            if velocity >= command_lst[k][0]: # 추가로 입력받은 가속도 값이 현재 속도보다 작다면
                velocity -= command_lst[k][1] # 속도에 가속도를 빼준다
            else: # 추가로 입력받은 가속도 값이 현재 속도보다 크다면 
                velocity = 0 # 속력을 0으로 초기화

        move += velocity # 현재 속도 * 1초 만큼 움직이므로 더해준다
    
    print('#{} {}'.format(i+1, move)) # 테스트 케이스 번호와 움직인거리를 출력한다