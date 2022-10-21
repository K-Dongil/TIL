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

#===============================================
tc = int(input())

for t in range(tc):
    nRange, nSelect = map(int, input().split())
    nList = list(map(int, input().split()))
    sumMaxV = 0
    sumMinV = 100 * 10000 * 10

    for i in range(0, nRange-nSelect+1):
        nowSumV = 0
        for j in range(nSelect):
            nowSumV += nList[i+j]
        if sumMaxV < nowSumV:
            sumMaxV = nowSumV
        if nowSumV < sumMinV:
            sumMinV = nowSumV

    diffV = sumMaxV - sumMinV
    print('#{} {}'.format(t+1, diffV))