# lst = list(range(1000000))
decimal_lst = [1] * 500000

for i in range(2, 500001):
    for j in range(2, i):
        if not i % j:
            decimal_lst[i] = 0

for i in range(500000):
    if decimal_lst[i]:
        print(i, end=" ")
        