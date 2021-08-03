# T = int(input()) # 테스트케이스 수 입력받음

# for i in range(T): # 위에 입력받은 값만큼 반복
#     word = input() # 문자를 입력받는다
#     str_list = [] # 문자의 알파벳들을 담을 빈 리스트

#     for j in range(len(word)-1, -1, -1): # 뒤에 있는 알파벳부터 차례대로 불러올 것이다
#         str_list.append(word[j]) # 리스트에 추가
#     uncertain_palindrome = ''.join(str_list) # 리스트에 들어있는 알파벳들을 하나로 합쳐 문자열을 만들어 변수에 저장

#     if word == uncertain_palindrome: # 만약 입력받은 문자와 뒤로 뒤집은 문자가 같다면
#         print('#{} 1'.format(i+1)) # 테스트케이스 번호와 1을 출력
#     else: # 만약 입력받은 문자와 뒤로 뒤집은 문자가 다르다면
#         print('#{} 0'.format(i+1)) #테스트케이스 번호와 0을 출력

T = int(input())

for i in range(T):
    word = input()
    reverse_word = word[-1:-len(word)-1:-1]
    if word == reverse_word:
        print('#{} 1'.format(i+1))
    else:
        print('#{} 0'.format(i+1))
