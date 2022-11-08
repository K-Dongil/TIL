start, end = map(int, input().split())
decimal = [True] * (end + 1)
decimal[0] = False
decimal[1] = False

for i in range(2, end+1):
    if decimal[i]:
        for j in range(i*2, end+1, i):
            decimal[j] = False

for i in range(end+1):
    if start <= i and decimal[i]:
        print(i)