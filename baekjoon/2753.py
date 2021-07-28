year = int(input()) # 입력값을 받는다
if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)): # 4의 배수이면 True(다음 값과 비교, 100의 배수가 아닐 때 True or 400의 배수일 때 True) 아니면 False(조건식 False), 
    print('1')
else:
    print('0') 