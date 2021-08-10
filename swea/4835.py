T = int(input())

for i in range(T):
    n, n_section = map(int, input().split())
    numbers = list(map(int, input().split()))
    sum_list = []

    for j in range(len(numbers)-n_section+1):
        sum = 0
        for k in range(0, n_section):
            sum += numbers[j+k]
        sum_list.append(sum)

    for head in range(len(sum_list)-1):
        for body in range(head+1, len(sum_list)):
            if sum_list[head] > sum_list[body]:
                sum_list[head], sum_list[body] = sum_list[body], sum_list[head]

    print('#{} {}'.format(i+1, sum_list[-1] - sum_list[0]))