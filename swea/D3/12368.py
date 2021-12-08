tc = int(input())

for t in range(1, tc+1):
    aPart, bPart = map(int, input().split())
    timeInClock = aPart + bPart
    if not timeInClock % 24:
        timeInClock = 0
    else:
        timeInClock = timeInClock % 24

    print(f'#{t} {timeInClock}')