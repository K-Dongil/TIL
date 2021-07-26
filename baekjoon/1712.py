import sys
A, B, C = map(int, sys.stdin.readline().split()) # A, B, C 를 int형태로 입력 받는다, 입력값은 총 3개의 숫자
if B >= C: # 만약 B가 C보다 크거나 같으면
    print(-1)  # -1출력
else: # 아니라면
    print(A//(C-B)+1) # A를 (B-C)로 나눈 몫에서 +1, A + Bx < Cx 이므로 
#==============================A================
# import sys
# A, B, C = map(int, sys.stdin.readline().split())
# count = 0
# while True:
#     count += 1
#     if A+B*count < C*count:
#         print(count)
#         break
#     elif 2100000000 <= C*count or B >= C:
#         print(-1)
#         break