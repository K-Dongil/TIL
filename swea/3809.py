tc = int(input())
for t in range(tc):
    N = int(input())
    str_num = ''

    while len(str_num) != N:
        str_num += ''.join(input().strip().split())

    idx = 0

    while True:
        if str(idx) not in str_num:
            break
        idx += 1 
    
    print(f'#{t+1} {idx}')