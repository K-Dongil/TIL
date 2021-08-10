t = int(input()) # 테스트 케이스 개수 입력받는다

for i in range(t): # 테스트 케이스 개수만큼 반복
    n = int(input()) # 몇 개의 숫자를 입력받을건지 입력받는다
    n_list = list(map(int, input().split())) # n개만큼 숫자를 입력받는다

    # 오름차순 정렬
    swap = False # swap이 일어나지 않을경우 for문 break줘서 O(n**2)보다는 완화
    for j in range(n-1):
        if swap:
            break
        swap = True 
        for k in range(j, n):
            if n_list[j] > n_list[k]:
                n_list[j], n_list[k] = n_list[k], n_list[j]
                swap = False

    print('#{} '.format(i+1), end='') # 테스트케이스 번호를 출력하는데 기본값인 \n을 없애준다 

    # print(*리스트) 로 출력하면 각 데이터 값을 띄어쓰기 기준으로 출력해준다
    for n in range(len(n_list)): # 입력받은 숫자의 개수만큼 반복
        if n == len(n_list)-1: # n이 n_list의 마지막 인덱싱 번호라면
            print(n_list[n]) # 개행문자 \n을 통해 다음 테스트케이스랑 구분하게 출력
        else: # n이 n_list의 마지막 인덱싱 번호가 아니라면
            print(n_list[n], end=' ') # n_list의 n번째 데이터값을 \n대신 띄어쓰기와같이 출력