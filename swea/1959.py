T = int(input()) # 테스트 케이크 개수 입력받음

for i in range(T): # 테스트 케이스 개수만큼 for문 반복
    list1_len, list2_len = map(int, input().split()) # 두개의 숫자열이 각각 몇개로 이루어져 있는지 입력 받는다

    list1 = list(map(int, input().split())) # A 숫자열의 구성
    list2 = list(map(int, input().split())) # B 숫자열의 구성

    sum_list = [] # A와 B의 서로 마주보는 값을 곱한 뒤 더한 값을 담아준다 (마주보는 위치를 바꿔준다)

    if list1_len <= list2_len: # 만약 A가 B보다 짧다면
        for j in range(list2_len-list1_len+1): # 마주보는 위치를 바꿔줄 수 있는 횟수, j를 움직인 거리라고 생각했다
            sum = 0 # 곱한 뒤 더한 값을 담아줄 변수
            for k in range(list1_len): # 두 값을 서로 곱한 뒤 더해주기 위해 A와 B 둘 중 짧은 숫자열을 고른다 
                sum += list1[k] * list2[k+j] # 더 짧은 A는 변화가 없고 더 긴 B를 움직였을 때를 대비해 k+j(움직인 거리)
            sum_list.append(sum) # B가 움직인 거리에 대해 값이 다를 것이므로 나중에 어떤 값이 가장큰지 비교하기 위해 리스트에 담아준다

    elif list1_len > list2_len: # 만약 B가 A보다 짧다면
        for j in range(list1_len-list2_len+1):
            sum = 0
            for k in range(list2_len):
                sum += list2[k] * list1[k+j]
            sum_list.append(sum)

    sum_list.sort() # 움직인 거리에 대해 결과값들이 list에 담겨져 있으므로 오름차순 sort를 한다
    print(f'#{i+1} {sum_list[-1]}') # 테스트케이스 번호와 오름차순 되어있는 리스트의 맨 뒤의 값을 가져온다.