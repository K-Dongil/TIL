tc = int(input()) # 테스트케이스 수 입력 받음

for t in range(tc): # 테스트케이스 수만큼 반복
    str = input() # 문자열 입력받음
    str_lst = [0]*4 # 각 문자들을 분리하여 List에 저장하기 위함
    result = '' # 결과값이 넣어질 공간

    # 문자들을 리스트에 저장
    for i in range(len(str)):
        str_lst[i] = str[i]
    
    # 문자 종류는 2개여야 하므로, List에 담겨진 문자 수를 확인하여 결과값 도출
    for l in str_lst: # 리스트에 담긴 값을 임시변수 l에 담아 반복
        if str_lst.count(l) != 2: # 문자가 담긴 l이 List에서 2개가 아닐 시 결과값은
            result = 'No' # 'No'
            break # 그 즉시 멈춘다
    else: # 만약 for문을 돌리는 동안 break가 실행되지 않았다면
        result = 'Yes' # 문자열은 문자의 종류가 2개, 각 문자는 2개씩 존재

    print(f'#{t+1} {result}') # 테스트케이스 번호와, 결과값 출력