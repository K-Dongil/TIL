T = int(input())

for i in range(T):
    n = int(input())
    num_list = list(map(int, input().split()))
    for j in range(len(num_list)):
        for k in range(j+1, len(num_list)):
            if num_list[j] > num_list[k]:
                num_list[j], num_list[k] = num_list[k], num_list[j]
    print(f'#{i+1} {num_list[-1]-num_list[0]}')




