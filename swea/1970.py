money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

tc = int(input())

for t in range(1, tc+1):
    pay = int(input())
    change = [0] * len(money)

    for i in range(len(money)):
        change[i] = str(pay // money[i])
        pay %= money[i]

    result = ' '.join(change)

    print(f'#{t}')
    print(result)