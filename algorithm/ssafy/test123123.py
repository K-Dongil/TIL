hexa_dict = {
    '0': 0, '1': 1, '2': 2,
    '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8,
    '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12,
    'D': 13, 'E': 14, 'F': 15
}

# 각 16진수를 2진수로 바꿔 반환해준다.
def bit(hexa):
    result = ''

    # 16진수를 10진수로 바꾸기
    deci = hexa_dict[hexa]

    # 10진수를 2진수로 바꾸기
    for i in range(3, -1, -1):
        if deci & (1 << i):
            result += '1'
        else:
            result += '0'
    return result

# 1의 연속된 개수가 1개 부터 9개까지 몇개까지 있는지 알아보기 위함
def counting(str):
    cnt = 0
    for s in str:
        if s == '1':
            cnt += 1
        if s == '0':
            if cnt:
                cnt_lst[cnt - 1] += 1
            cnt = 0
    if cnt:
        cnt_lst[cnt - 1] += 1


T = int(input())

for t in range(1, T+1):
    hexa_len = int(input())
    hexa_str = input()
    binary = ''
    cnt_lst = [0] * 9

    for hexa in hexa_str:
        binary += bit(hexa)

    counting(binary)

    # 출력을 위해 cnt_lst에 있는 int형들을 str형들로 바꿈
    for i in range(9):
        cnt_lst[i] = str(cnt_lst[i])

    print('#{} {}'.format(t, ' '.join(cnt_lst)))