dic = {
    '1': [], '2':['a','b','c'], '3':['d','e','f'],
    '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'],
    '7':['p','q','r', 's'], '8':['t', 'u', 'v'], '9':['w','x', 'y', 'z']
}

tc = int(input())

for t in range(1, tc+1):
    press_num, word_num = input().split()
    words = input().split()
    cnt = 0

    for word in words:
        for i in range(len(press_num)):
            if not word[i] in dic[press_num[i]]:
                break
        else:
            cnt += 1

    print(f'#{t} {cnt}')
