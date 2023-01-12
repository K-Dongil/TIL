coinNum, price = map(int, input().split())
coins = [int(input()) for _ in range(coinNum)]
cnt = 0

for coin in coins[::-1]:
    if price // coin:
        cnt += price // coin
        price %= coin

print(cnt)