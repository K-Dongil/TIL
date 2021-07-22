import sys
C = int(input()) # 테스트 케이스 개수
for i in range(C):
    totalScore = 0 # 학생들의 총점
    highStudent = 0 # 평균보다 높은 학생들 수
    avg_score = 0 #평균 점수
    a = list(map(int, sys.stdin.readline().split())) # list형태로 학생수와 학생들의 점수 입려 받기
    for j in range(1, len(a)): # 학생 수 만큼 for문 돌린다
        totalScore += a[j] # 각 학생들의 점수를 더함
        if j == len(a)-1: # 마지막 학생의 점수를 더하고난 뒤 
            avg_score = totalScore/(len(a)-1)  # 평균을 구한다
    else: #for문이 끝나면(평균을 구했으면)
        for k in range(1, len(a)): # 학생수만큼 for문을 다시 돌린다
            if a[k] > avg_score: # 평균보다 높은 점수를 찾는다
                highStudent += 1 # 평균보다 높으면 counting
        else: # counting이 끝나면
            print('%0.3f' %(highStudent/a[0]*100) +'%') # 비율을 반올림하여 소수점 3째자리까지 출력한다