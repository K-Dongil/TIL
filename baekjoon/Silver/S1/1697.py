def bfs(start):
    queue = [start]
    while queue:
        now = queue.pop(0)
        if now == finishPoint:
            print(times[finishPoint])
            break
        for nextPoint in (now-1, now+1, 2*now):
            if 0<=nextPoint<N and times[nextPoint] == 0:
                times[nextPoint] = times[now]+1
                queue.append(nextPoint)

nowPoint, finishPoint = map(int, input().split())
N = 100001
times = [0] * (100001)

bfs(nowPoint)