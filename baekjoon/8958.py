import sys
N = int(input()) #테스트 케이스 개수
ox_list = [] # OX퀴즈 담을 빈 리스트
for i in range(N): #테스트 케이스 개수만큼 
    ox_list.append(input()) # 입력 받겠다.
for i in range(N):
    total_score = 0 #총 점수
    score = 0 # 퀴즈 O,X 여부에 따라 더할 점수
    for j in range(len(ox_list[i])): # OX퀴즈 결과만큼 for문을 돌린다
        if ox_list[i][j] == 'O': # 퀴즈 결과가 O일 때
            score += 1 # 연속된 O의 개수가 점수이므로 score 점수를 +1 씩 해줌
            total_score += score 
        elif ox_list[i][j] == "X": # 퀴즈 결과가 X일 때
            score = 0 # 연속된 O의 개수는 0개가 되므로 score점수 초기화
    else:
        print(total_score) # 한 개의 테스트 케이스가 끝난다면 최종점수 출력

#--------------------------------------------
# import sys
# N = int(input()) #테스트 케이스 개수
# ox_list = [] # OX퀴즈 담을 빈 리스트
# for i in range(N): #테스트 케이스 개수만큼 
#     ox_list.append(input()) # 입력 받겠다.
# for i in range(N):
#     total_score = 0 #총 점수
#     score = 0 # 퀴즈 O,X 여부에 따라 더할 점수
#     for j in range(len(ox_list[i])):
#         if ox_list[i][j] == 'O':
#             score += 1
#             total_score += score
#         elif ox_list[i][j] == "X":
#             score = 0
#         if j == len(ox_list)-1:
#             print(total_score)