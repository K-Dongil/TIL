englishStr = input() # 문자열 입력받는다
spaceStr = ' ' # 입력받은 문자열에서 단어를 셀 때 기준이 되는 공백을 변수에 초기화 (단 입력받은 문자열에서 공백이 연속으로 나오지 않는다)
wordNum = 1 # 단어의 갯수를 1로 설정해놓은 이유 : 스페이스를 기준으로 단어 개수를 셀 때는 한개의 단어를 입력받았을 때는 공백으로 구분 불가
for i in englishStr: # 문자열에 있는 문자들을 변수 i에 담아 for문 돌리기
    if i == spaceStr: # 만약 문자가 공백이라면
        wordNum += 1 # 단어 개수를 세는 변수에 +1
if englishStr[0] == ' ': # 만약 문자열의 앞이 공백이라면
    wordNum -= 1 # 단어 개수 -1
if englishStr[len(englishStr)-1] == ' ': # 만약 문자열의 맨 뒤가 공백이라면
    wordNum -= 1 #단어 개수 -1
print(wordNum) # 단어 개수 출력