tc = int(input()) # 테스트 케이스 수 입력받는다

for t in range(tc): # 테스트 케이스 수만큼 반복
    N = int(input()) # 건초더미 개수 입력받는다
    sizes = [0] * N # 건초더미 사이즈 data가 담길 List
    move = 0 # 몇번 움직이는지 data가 담길 공간
    avg_size = 0 # 원래 건초더미의 크기를 저장해놓을 공간

    for i in range(N): # 건초더미 개수만큼 반복
        sizes[i] = int(input()) # List에 각 건초더미의 크기의 data를 저장

    for size in sizes: # 리스트에 담긴 값들을 차례대로 가지고 반복
        avg_size += size # avg_size 변수에 더해준다
    avg_size //= N # 원래 건초더미의 크기를 구한다

    # 원래 건초더미의 크기는 전부 같다 -> 현재 건초더미 - 원래 건초더미의 크기 = 움직여야할 횟수 (음수값 제외)
    for size in sizes:
        if avg_size < size:
            move += size - avg_size

    print(f'#{t+1} {move}') # 테스트케이스 수와 결과값 출력

# # 시간초과
# def bubble_sort(lst):
#     for i in range(len(lst)):
#         for j in range(i, len(lst)-1):
#             if lst[j] < lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]

# tc = int(input())

# for t in range(tc):
#     N = int(input())
#     sizes = [0] * N
#     move = 0

#     for i in range(N):
#         sizes[i] = int(input())

#     while True:
#         bubble_sort(sizes)
#         if sizes[0] == sizes[-1]:
#             break
#         sizes[0] -= 1
#         sizes[-1] += 1
#         move += 1

#     print(f'#{t+1} {move}')
