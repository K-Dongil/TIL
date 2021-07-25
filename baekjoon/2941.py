croatiaStr = input() # 문자열 입력받는다
croatiaList = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 특수한 크로아티아 알파벳을 리스트에 저장
for i in croatiaList: # 크로아티아 알파벳들을 차례대로 변수 i에 담아 for문 돌린다
    croatiaStr = croatiaStr.replace(i, '1') # 만약 문자열에 크로아티아 변수가 있다면 1로 변환
print(len(croatiaStr)) # 변환된 문자열의 길이를 출력하여 몇 개의 크로아티아 알파벳으로 이루어져 있는지 확인