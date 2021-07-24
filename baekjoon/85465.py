S = input() # 문자 입력받음
alphabet = 'abcdefghijklmnopqrstuvwxyz' # 입력받은 문자와 알파벳 비교하기 위해 알파벳을 변수에 초기화
for i in alphabet: # 알파벳 개수만큼 for문을 반복
    if i in S: # 알파벳이 입력받은 문자안에 있다면
        print(S.index(i), end=' ') # 문자열의 몇번째 index에 위치해있는지 출력
    else: # 알파벳이 입력받은 문자안에 없다면
        print(-1, end=' ') # -1 출력