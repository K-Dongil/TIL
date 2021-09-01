tc = int(input()) # 테스트케이스 개수 입력받는다

for t in range(tc): # 테스트케이스 개수만큼 반복
    L, U, X = map(int, input().split()) # 최소 목표운동시간, 최대 목표운동시간, 실제 운동시간
    more_exercise = 0 # 더 해야하는 운동시간
    if X < L: # 만약 실제 운동시간이 최소 운동시간보다 작다면
        more_exercise = L - X # 더 해야하는 운동시간 = 최소 목표운동시간 - 실제운동시간
    elif U < X: # 만약 최대 목표 운동시간보다 실제 운동시간이 더 길다면
        more_exercise = -1 # -1로 초기화
    
    print('#{} {}'.format(t+1, more_exercise)) # 테스트케이스 번호와, 얼마나 더 해야하는지 출력