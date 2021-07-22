selfNumList = list(range(1, 10001)) # 1~10000가 들어있는 리스트 생성
emptyList = [] # 생성자가 있는 숫자들 담을 비어있는 리스트 생성
def selfNumber(num): # 1~ 10000까지의 숫자들을 매개변수로 받음
    strNum = str(num) # 숫자에서 문자열 형태로 바꿔서 변수에 저장
    for i in strNum: # 문자열에 담긴 문자들을 임시변수 i에 담아 줘서 for문을 돌림
        num += int(i) # selfnumber아닌 값이 생성, 자기자신+ 각 자리의 숫자 더해 줌
    return num 
for i in selfNumList: # selfNumList의 데이터 수만큼
    removeNum = selfNumber(i) # sefNumber 함수 호출하는데 리스트에 담겨진 데이터들을 인자로 넘겨줌, 그리고 셀프넘버 아닌 것들을 return받음
    if removeNum <= 10000: # selfNumList에 담긴 숫자보다 큰 숫자들은 제외
        emptyList.append(removeNum) # 생성자가 있는 숫자들을 리스트에 담아줌
emptySet = set(emptyList) #중복값 제거위해 set형식으로 바꿈
for i in emptySet: # 생성자가 있는 숫자들을
    selfNumList.remove(i) # 리스트에서 제거
for i in selfNumList:
    print(i) #한 줄씩 출력