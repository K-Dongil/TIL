T = 10  # 테스트 케이스 개수

for i in range(T):  # 테스트 케이스 개수만큼 반복한다
    N = int(input())  # 각 아파트의 층수를 입력 받는다
    n_list = list(map(int, input().split()))  # 각 아파트의 층수를 입력 받는다
    count = 0  # 왼쪽으로 2칸 오른쪽으로 2칸 조망권이 확보되는 층수를 기록하는 변수

    for j in range(2, len(n_list) - 1):  # 왼쪽, 오른쪽 2칸은 모두 0층이므로 범위를 이렇게 결정

        if n_list[j - 2] < n_list[j] and n_list[j - 1] < n_list[j] and n_list[j] > n_list[j + 1] and n_list[j] > n_list[
            j + 2]:  # 앞 1, 2칸 뒤 1,2칸보다 가운데 층이 크다면 조망권이 확보된 것이므로
            neighborhood_list = [n_list[j - 2], n_list[j - 1], n_list[j + 1], n_list[j + 2]]  # 앞, 뒤 1,2칸들을 리스트에 담아 준다

            for bubble in range(len(neighborhood_list)):  # 앞 뒤 1,2칸 들을 버블정렬을 통해 오름차순 시킨다
                for sort in range(bubble, len(neighborhood_list)):
                    if neighborhood_list[bubble] > neighborhood_list[sort]:
                        neighborhood_list[bubble], neighborhood_list[sort] = neighborhood_list[sort], neighborhood_list[
                            bubble]

            count += n_list[j] - neighborhood_list[-1]  # 가운데 층에서 이웃 층중 가장 높은 층을 빼면 조망권이 몇층이 확보되어있는지 알 수 있다

    print('#{} {}'.format(i + 1, count))  # 테스트 케이스 번호와 조망권이 확보된 층수를 출력