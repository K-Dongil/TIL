import sys
N = int(input()) # int형으로 입력 받음
num = input() # str형으로 입력받음
total = 0 # 입력값 더할 공간
for i in num: # 문자열 길이만큼 for문 반복
    total += int(i) # 문자열 인덱싱 처음부터 끝까지 호출해서 int형으로 바꾼 뒤 더하기
print(total)