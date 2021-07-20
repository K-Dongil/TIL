L = [] # 입력받은 값들을 저장할 빈 리스트 생성
count = 0 # 최대값이 몇번째 값인지 셀 변수
for i in range(9): # 9번동안 반복
    L.append(int(input())) # 비어있는 리스트에 입력값 append
print(max(L)) # 최대값 출력
for i in enumerate(L): # enumerate는 리스트의 index 번호와 value를 출력
    if i[1] == max(L): # tuple형태에서 value값은 index 1에 존재
        print(count+1) # index번호는 0부터 세고 순서 셀 때는 1부터 세니 +1 해줌
        break
    count += 1 # if문이 실행안되면 count 