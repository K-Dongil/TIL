A = int(input())
B = int(input())
C = int(input())
D = A*B*C #입력받은 값들의 곱셈 결과값 D에 초기화
ABC =[] # 위에서 나온 결과를 담을 빈 리스트
for i in str(D): #문자열 길이만큼 for문 반복
    ABC.append(i) #문자열의 문자들을 ABC리스트에 담아 줌
ABC = list(map(int, ABC)) # list(map(int, ABC))를 다시 ABC 변수에 초기화
#print(type(ABC[0])) 타입 점검
for i in range(10): # 0~9
    count = 0 # 0~9까지 A*B*C결과에 몇번 쓰였는지 counting변수, 숫자가 바뀔 때 마다 0으로 초기화
    for j in range(len(ABC)): # 리스트의 길이만큼  for문 반복
        if i == ABC[j]: # ABC리스트의 j번째 값이 i(0~9)와 같다면
            count += 1 # counting
    else:
        print(count)

# A = int(input())
# B = int(input())
# C = int(input())
# D = A*B*C
# ABC =[]
# for i in str(D):
#     ABC.append(i)
# ABC = list(map(int, ABC))
# for i in range(10):
#     count = 0
#     for j in range(len(ABC)):
#         if i == ABC[j]:
#             count += 1
#         if j == len(ABC)-1:
#             print(count)