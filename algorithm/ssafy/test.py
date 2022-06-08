def binaryS(key, lst): # key는 찾고자 하는 값
    l = 0
    r = 0
    start = 0
    end = len(lst) - 1
    while start <= end:
        m = (start+end)//2
        if key == lst[m]: # 검색성공
            if 0 < l and 0 < r:
                return 1
            else:
                return 0
        elif key < lst [m]:
            end = m - 1 # 주의!!
            l += 1
        else:
            start = m +1 # 주의!!
            r += 1

    if 0 < l and 0 < r:
        return 1
    else:
        return 0

tc = int(input())

for t in range(1, tc+1):
    N, M = map(int, input().split())

    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    count = 0

    for b in b_lst:
        count += binaryS(b,a_lst)

    print(f'#{t} {count}')