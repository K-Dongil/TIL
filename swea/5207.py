# * 주의 : 오른쪽 왼쪽 왼쪽 오른쪽
def binaryS(key, lst): # key는 찾고자 하는 값
    direction = ''
    start = 0
    end = len(lst) - 1
    while start <= end:
        m = (start+end)//2
        if key == lst[m]: # 검색성공
            return 1
        elif key < lst [m]:
            end = m - 1 # 주의!!
            if direction == 'left':
                return 0
            direction = 'left'
        else:
            start = m +1 # 주의!!
            if direction == 'right':
                return 0
            direction = 'right'

    return 0

tc = int(input())

for t in range(1, tc+1):
    N, M = map(int, input().split())

    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    a_lst.sort()
    count = 0

    for b in b_lst:
        count += binaryS(b,a_lst)

    print(f'#{t} {count}')