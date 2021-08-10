# 리스트를 오름차순 시켜주는 함수
def bubble_sort(lst):
    for j in range(len(lst)-1):
        for k in range(j, len(lst)):
            if lst[j] > lst[k]:
                lst[j], lst[k] = lst[k], lst[j]
    return lst

T = 10 # 테스트 케이스 개수

for i in range(T):
    dump_chance = int(input())
    height_list = list(map(int, input().split()))
    gap = 0

    while dump_chance != 0:

        height_list = bubble_sort(height_list)

        long_height = height_list[-1]
        short_height = height_list[0]
        gap = long_height - short_height

        if gap > 1:
            height_list[-1] -= 1
            height_list[0] += 1
        elif gap <= 1:
            break

        dump_chance -= 1

    height_list = bubble_sort(height_list)
    long_height = height_list[-1]
    short_height = height_list[0]
    gap = long_height - short_height

    print('#{} {}'.format(i+1, gap))

    # 버블sort는 n**2 max나 min을 썻으면 좋았을 것 같다.