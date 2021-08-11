# 퍼즐의 가로 부분에서 단어를 넣을 수 있는 공간이 몇개인지 세어줄 함수
def row_sum(lst, word_len): # 길이가 입력받은 단어의 길이만큼인 row을 찾아주는 함수, 매개변수로는 리스트와 단어의 길이를 받는다
    chance = 0 # 퍼즐에서 공간이 word_len만큼 딱 맞아 떨어지는 곳을 count해주는 공간 

    for row in range(len(lst)): # 리스트의 row 수 만큼 반복
        sum = 0 # 퍼즐에서 흰색 부분이 어느정도 이어져있는지 저장해놓을 공간
        for col in range(len(lst[0])): # 리스트의 column 수 만큼 반복
            if lst[row][col] ==1: # 만약 불러온 값이 흰부분이라면
                sum += lst[row][col] # 지금까지의 흰색 부분이 얼만큼인지 저장되어있는 sum을 +1
            else: # 만약 불러온 값이 검정부분일 때
                if sum == word_len: # 지금까지의 흰색부분이 word_len(원하는 단어의 길이)만큼이라면
                    chance +=1 # 단어를 넣을 수 있는 공간이 1개 늘어난다
                sum = 0 # 그리고 흰색 부분을 0로 초기화
            if col == len(lst[0])-1: # 만약 퍼즐의 마지막 부분일 때
                if sum == word_len: # 흰색 부분이 word_len만큼이라면
                    chance += 1 # 단어를 넣을 수 있는 공간이 1개 늘어난다

    return chance # 원하는 길이의 단어를 몇개 넣을 수 있는지 return

# 퍼즐의 세로 부분에서 단어를 넣을 수 있는 공간이 몇개인지 세어줄 함수
def col_sum(lst, word_len): # 길이가 입력받은 단어의 길이만큼인 column을 찾아주는 함수, 매개변수로는 리스트와 단어의 길이를 받는다
    chance = 0 # 퍼즐에서 공간이 word_len만큼 딱 맞아 떨어지는 곳을 count해주는 공간

    for col in range(len(lst[0])): # 리스트의 col 수 만큼 반복
        sum = 0 # 퍼즐에서 흰색 부분이 어느정도 이어져있는지 저장해놓을 공간
        for row in range(len(lst)):
            if lst[row][col] ==1: # 만약 불러온 값이 흰부분이라면
                sum += lst[row][col] # 지금까지의 흰색 부분이 얼만큼인지 저장되어있는 sum을 +1
            else: # 만약 불러온 값이 검정부분일 때
                if sum == word_len: # 지금까지의 흰색부분이 word_len(원하는 단어의 길이)만큼이라면
                    chance +=1 # 단어를 넣을 수 있는 공간이 1개 늘어난다
                sum = 0 # 그리고 흰색 부분을 0로 초기화
            if row == len(lst)-1: # 만약 퍼즐의 마지막 부분일 때
                if sum == word_len: # 흰색 부분이 word_len만큼이라면
                    chance += 1# 단어를 넣을 수 있는 공간이 1개 늘어난다

    return chance # 원하는 길이의 단어를 몇개 넣을 수 있는지 return

t = int(input()) # 테스트케이스 개수 입력받는다

for i in range(t): # 테스트케이스만큼 반복
    square, word_len = map(int, input().split()) # 퍼즐(정사각형)의 길이와 단어의 길이를 입력받는다
    square_lst = [list(map(int, input().split())) for _ in range(square)] # 퍼즐에서 흰색 부분과 검정색 부분을 입력받는데, square번 입력받는다, listComprehension

    row_chance = row_sum(square_lst, word_len) # 퍼즐의 가로에서 원하는 길이의 단어를 몇개 넣을 수 있는지 return받아 공간에 저장
    col_chance = col_sum(square_lst, word_len) # 퍼즐의 세로에서 원하는 길이의 단어를 몇개 넣을 수 있는지 return받아 공간에 저장
    total_chance = row_chance + col_chance # 가로+세로에서 몇 개를 넣을 수 있는지 저장

    print('#{} {}'.format(i+1, total_chance)) # 테스트케이스 번호와 총 몇개를 넣을 수 있는지 출력




def row_sum(lst, word_len):
    chance = 0
    for row in range(len(lst)):
        sum = 0
        for col in range(len(lst[0])):
            if lst[row][col] ==1:
                sum += lst[row][col]
            else:
                if sum == word_len:
                    chance +=1
                sum = 0
            if col == len(lst[0])-1:
                if sum == word_len:
                    chance += 1
    return chance

def col_sum(lst, word_len): # 길이가 입력받은 단어의 길이만큼인 column을 찾아주는 함수, 매개변수로는 리스트와 단어의 길이를 받는다
    chance = 0
    for col in range(len(lst[0])):
        sum = 0
        for row in range(len(lst)):
            if lst[row][col] ==1:
                sum += lst[row][col]
            else:
                if sum == word_len:
                    chance +=1
                sum = 0
            if row == len(lst)-1:
                if sum == word_len:
                    chance += 1
    return chance

t = int(input())

for i in range(t):
    square, word_len = map(int, input().split())
    square_lst = [list(map(int, input().split())) for _ in range(square)]

    row_chance = row_sum(square_lst, word_len)
    col_chance = col_sum(square_lst, word_len)
    total_chance = row_chance + col_chance

    print('#{} {}'.format(i+1, total_chance))