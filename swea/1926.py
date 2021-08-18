n = int(input()) # 숫자를 입력받는다.

for i in range(1, n+1): #  1 ~ n까지 임시변수 i에 담아 반복한다
    count = 0 # 숫자에 3, 6, 9 가 들어있는지 판별해줄 변수
    for s in str(i): # 숫자를 문자열로 변환 후 각 문자들을 임시변수 s에 담아 반복 
        if s == '3' or s == '6' or s == '9': # 만약 문자가 3 or 6 or 9라면
            count += 1 # counting 해주는 변수에 1을 더해주고
    if count != 0: # 만약 숫자에 3, 6, 9 가 포함되어있는지 확인해주는 변수가 0이 아니라면
        print(count * '-', end=' ') # -를 출력과 동시에 띄어쓰기를 위한 출력
    else: # 만약 숫자에 3, 6, 9 가 포함되어 있지 않다면 
        print(i, end=' ') # 숫자를 그대로 출력한 뒤 띄어쓰기


# # 다른분코드
# n = int(input())

# clap = ['3', '6', '9']

# for i in range(1, n+1):
#     cnt = 0
#     for j in str(i):
#         if j in clap:
#             cnt += 1
#     if cnt > 0:
#         i = '-'*cnt

#     print(i, end=' ')