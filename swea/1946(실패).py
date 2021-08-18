tc = int(input())

for t in range(tc):
    N = int(input())
    alphabet_lst = [list(input().split()) for _ in range(N)]
    remain_count = 0
    a = alphabet[1] // 10


    for alphabet in alphabet_lst:
        if remain_count > 0:
            print(alphabet[0] * remain_count)
        remain_count += int(alphabet[1]) - 10
        if remain_count >= 0:
            print(alphabet[0] * int(alphabet[1]) , end='')
        else:
            print(alphabet[0] * 10)
            if remain_count == 10:
                print(alphabet[0] * 10)
                remain_count = 0