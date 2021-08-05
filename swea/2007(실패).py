T = int(input())

for i in range(T):
    long_str = input()

    count = 0
    
    for s in range(3, len(long_str)-4):
        if long_str[0] == long_str[s] and long_str[1] == long_str[s+1] and long_str[2] == long_str[s+2]:
            count +=1
    print(f'#{i+1} {count}')