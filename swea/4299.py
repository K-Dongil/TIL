tc = int(input()) # 테스트 케이스 수 입력받는다
meeting_D = 11 # 약속 시간's DAY
meeting_H = 11 # 약속 시간's HOUR
meeting_M = 11 # 약속 시간's Minute

for t in range(tc): # 테스트 케이스 수만큼 반복
    D, H, M = map(int, input().split()) # 날짜, 몇시, 몇분 입력 받는다

    diff_D = D - meeting_D # 만나기로한 날짜와 깨달음을 얻은 날짜의 차이
    diff_H = H - meeting_H # 만나기로한 시간과 깨달음을 얻은 시간의 차이
    diff_M = M - meeting_M # 만나기로한 시간과 깨달음을 얻은 시간의 차이
 
    effort_M = diff_D * (24*60) + diff_H * 60 + diff_M # 분으로 표시

    if effort_M < 0: # 만약 깨달음을 만나기로한 시간보다 일찍 얻었다면
        effort_M = -1 # 결과값은 -1
    print(f'#{t+1} {effort_M}') # 테스트 케이스 수와 결과값 출력