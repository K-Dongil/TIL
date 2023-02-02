N = int(input())
times = list(map(int, input().split()))
times.sort()
waitingTime = 0
result = 0

for time in times:
    waitingTime += time
    result += waitingTime

print(result)