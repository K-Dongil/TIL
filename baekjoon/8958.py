import sys
N = int(input()) #테스트 케이스 개수
ox_list = [] # OX퀴즈 담을 빈 리스트
for i in range(N): #테스트 케이스 개수만큼 
    ox_list.append(input()) # 입력 받겠다.
for i in range(N):
    total_score = 0 #총 점수
    score = 0 # 퀴즈 O,X 여부에 따라 더할 점수
    for j in range(len(ox_list[i])):
        if ox_list[i][j] == 'O':
            score += 1
            total_score += score
        elif ox_list[i][j] == "X":
            score = 0
        if j == len(ox_list)-1:
            print(total_score)
    # else:
    #     print(total_score)