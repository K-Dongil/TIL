tc = int(input()) # 테스트 케이스 수 입력 받는다

for t in range(tc): # 테스트 케이스 수만큼 반복
    time_lst = [list(map(int, input().split(':'))) for _ in range(2)] # 입력받은 값에서 :를 기준으로 data를 나눠 2차원 배열을 만든다
    promise = [0] * 3 # 약속시간까지 남은 시간을 저장할 list, 0번째에 hour 1번째에 minute 2번째에 sec

    if time_lst[0][0] < time_lst[1][0]: # 약속시간의 hour가 현재시간의 hour보다 뒤라면 오늘 만난다
        promise[0] = time_lst[1][0] - time_lst[0][0]
    else: # 약속시간이 현재시간보다 뒤라면 내일 만난다
        promise[0] = 24 - time_lst[0][0] + time_lst[1][0]

    for i in range(1, 3):
        promise[i] = time_lst[1][i] - time_lst[0][i]
    
    if promise[2] < 0: # 만약 s가 음의 값이라면
        promise[2] += 60 # s에 60초를 더하고
        promise[1] -= 1 # m에 1분을 뺀다
    
    if promise[1] < 0: # 만약 m가 음의 값이라면
        promise[1] += 60 # m에 60분을 더하고
        promise[0] -= 1 # h에 1시간을 뺀다

    # 만약 h, m, s가 일의자리수라면 요구하는 출력과 다르게 나오므로 앞에 0을 붙여준다
    for i in range(len(promise)):
        if promise[i] < 10:
            promise[i] = '0' + str(promise[i])

    
    print(f'#{t+1} {promise[0]}:{promise[1]}:{promise[2]}') # 테스트 케이스번호와 결과값 출력한다