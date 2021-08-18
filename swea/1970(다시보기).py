tc = int(input()) # 테스트케이스 개수 입력 받는다

for t in range(tc): # 테스트케이스 개수만큼 반복
    money = int(input()) # 거슬러 줘야하는 돈 입력받음
    money_unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10] # 가게에서 보유하고있는 현금단위들을 리스트에 담아준다
    money_unit_lst = [] # 각 단위의 돈을 몇개씩 나눠 줄지 저장해둘 비어있는 리스트

    for unit in money_unit: # 가게에서 보유하고 있는 현금단위를 unit이라는 변수에 담아 반복
        money_unit_lst.append(money // unit) # 가장 큰 현금단위부터 몇 개씩 줘야하는지 리스트에 추가
        money = money % unit # 남아있는 거슬러줘야 하는 돈
    
    print('#{}'.format(t+1)) # 테스트케이스 번호 출력
    print(*money_unit_lst) # 리스트에 담겨져있는 data값들을 띄어쓰기를 기준으로 출력
    # for i in money_unit_lst: # 각 단위의 돈들을 몇개씩 나눠줘야하는지 data를 변수 i에 담아 반복
    #     print(i, end=' ') # 출력하는데 end=' '를 사용하여 \t대신에 띄어쓰기
    # else: # for문 반복이 끝나면 
    #     print() # 다음 줄로 넘어갈 수 있게 print()