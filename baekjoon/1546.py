import sys
total_score = 0 
N = int(input()) # 시험 본 과목의 개수
score_list = list(map(int, sys.stdin.readline().split())) # 시험 본 과목의 점수들을 int타입인 list형태로 받아옴
max_score = max(score_list) # 점수 중 최대 값 변수에 담기
for i in range(len(score_list)): # 과목 갯수만큼 for문 돌리기
    score_list[i] = score_list[i]/max_score*100 
    total_score += score_list[i] # 새로운 평균 구하기 위한 총 점수 구하기
print(total_score/len(score_list)) # 총 점수를 시험 본 과목개수만큼 나눠서 평균 구하기