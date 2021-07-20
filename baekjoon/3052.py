a_list = [] # 입력 값을 저장할 빈 리스트
b_list = [] # 42로 나눈 나머지들을 저장한 빈 리스트
for i in range(10): # 10개의 데이터 입력할 것이므로 10번 반복
    a_list.append(int(input())) # 입력데이터 a_list에 추가
for i in range(len(a_list)): # 입력받은 데이터 갯수만큼 for문 반복
    b_list.append(a_list[i]%42) # 입력받은 데이터를 42로 나눈 나머지들을 b_list에 저장
print(len(set(b_list))) #b_list에서 중복값 제거하고 데이터의 갯수 확인