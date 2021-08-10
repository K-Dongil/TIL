# BubbleSort는 n**2 max나 min을 썻으면 좋았을 것 같다.
# 이 알고리즈의 단점은 반복적으로 max와 min의 처리를 위하여 dump 횟수만큼 O(n)을 수행했다.
# 줄일 수 있는 방법 : COUNT 배열 활용

# 리스트를 오름차순 시켜주는 함수
def bubble_sort(lst):
    for j in range(len(lst)-1):
        for k in range(j, len(lst)):
            if lst[j] > lst[k]:
                lst[j], lst[k] = lst[k], lst[j]
    return lst

T = 10 # 테스트 케이스 개수

for i in range(T): # 테스트 케이스만큼 반복
    dump_chance = int(input()) # 주어진 dump 횟수를 입력받는다
    height_list = list(map(int, input().split())) # 각 상자의 높이들을 입력받아 list에 담아준다
    gap = 0 # 밑의 코드에서 가장 큰 높이의 박스와 가장 낮은 높이의 박스의 차를 담아줄 변수

    while dump_chance != 0: # 덤프 기회가 0이 될 때까지 무한 반복 

        height_list = bubble_sort(height_list) # Bubble Sort를 이용해 높이에 대하여 오름차순 하였다

        long_height = height_list[-1] # 가장 높이가 큰 박스
        short_height = height_list[0] # 가장 높이가 낮은 박스
        gap = long_height - short_height # 높이가 큰 박스와 높이가 낮은 박스의 차이

        if gap > 1: # 차이가 1보다 클 때는
            height_list[-1] -= 1 # 가장 높이가 큰 박스에서
            height_list[0] += 1 # 가장 높이가 낮은 박스로 dump
        elif gap <= 1: # 차이가 1이하일 때
            break # while문을 빠져 나온다

        dump_chance -= 1 # dump가 실행되면 기회가 1만큼 줄어든 뒤 while문의 조건으로 올라간다

    height_list = bubble_sort(height_list) # dump 기회가 떨어질 때까지 while문이 돌아갔을 dataset에 대비하여 다시한번 정렬 후
    long_height = height_list[-1] # 가장 높은 박스의 높이와
    short_height = height_list[0] # 가장 낮은 박스의 높이를 구하여
    gap = long_height - short_height # 차이를 구한다

    print('#{} {}'.format(i+1, gap)) # 테스트케이스 번호와 dump후 상자의 gap을 구한다