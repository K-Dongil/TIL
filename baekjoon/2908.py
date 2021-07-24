import sys
numList = sys.stdin.readline().split() # 입력값을 공백을 기준으로 구분하여 리스트형태로 담아 줌 
newNumList = [] # 값을 거꾸로 바꾼 값을 담을 공간(List)
for i in numList: # 입력받은 값을 변수에 i에 담아주고 for문을 반복
    newNum ='' # 뒤집은 값을 저장할 변수, 여기에 초기화 시킨 이유는 for문이 한번씩 돌 때 마다 뒤집은 값이 저장된 변수를 재사용하기 위해
    for j in range(len(i)-1, -1, -1): # 문자열의 인덱싱번호를 거꾸로 읽기 위해
        newNum += i[j] 
    newNumList.append(newNum)
if newNumList[0] < newNumList[1]: # 뒤집은 두 값을 비교
    print(newNumList[1])
else:
    print(newNumList[0])
