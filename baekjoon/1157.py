strList = []
strInput = (input()).upper() # upper함수는 문자열에 있는 문자들을 모두 대문자로 만들어 줌
strSet = set(strInput) # 입력받은 문자열에 어떤 문자들이 있는지 확인하기 위한 중복제거
bestStr = '' # 가장 많이 입력된 문자를 저장할 변수
bestStrCount = 0 # 가장 많이 입력된 문자의 개수
for i in strSet: # 문자열에 존재하는 중복되지 않는 문자 갯수만큼
    strList.append((i, strInput.count(i))) # 문자와 문자의 갯수를 튜플형태로 리스트에 담아 줌 
for i in strList: # 리스트에 있는 데이터 갯수만큼 반복
    if bestStrCount < i[1]: # 가장 많이 입력된 문자의 개수가 현재 i에 담겨진 개수보다 작다면 
        bestStrCount = i[1] # i에 담겨진 개수를 변수에 초기화
        bestStr = i[0] # i에 담겨진 문자를 변수에 초기화
    elif bestStrCount == i[1]: # 만약 가장 많이 입력된 문자의 개수가 현재 i에 담겨진 개수랑 같다면
        bestStr = '?' # 변수에 ?문자를 초기화
print(bestStr) # 최고로 많이 입력된 문자를 출력