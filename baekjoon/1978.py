N = int(input()) # 주어진 숫자의 개수
numbers = list(map(int, input().split())) # 입력받은 값들을 공백을 기준으로 int형으로 변환하여 리스트형태로 담아준다
decimal = [] # 소수를 넣어 줄 리스트
for number in numbers: # 입력받은 값들을 차례대로 number라는 변수에 넣어 for문에 돌린다
    check = 0 # number의 인수를 세어줄 변수
    for i in range(1, number+1): # 1~ number의 숫자를 차례대로 임시변수 i에 담아 for문 돌려준다
        if not number % i: # 입력받은 값을 1~number로 나누었을 때 나머지가 0이라면
            check += 1 # 인수이므로 인수의 수를 세는 count에 1을 더해준다
    if check == 2: # 만약 인수가 2개면 소수이므로
        decimal.append(number) # 소수를 담을 리스트에 추가
print(len(decimal)) # 소수가 담겨있는 리스트의 길이를 출력