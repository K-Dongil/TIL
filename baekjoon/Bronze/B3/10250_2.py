from collections import deque

tc = int(input())

for t in range(tc):
    height, weight, nGuest = map(int, input().split())
    hotel = deque([list(range(1, height+1)) for _ in range(weight)])
    floor = 1
    ho = 1
    nowFloor = deque(hotel.popleft())

    while 0 < nGuest:
        nGuest -= 1
        if len(nowFloor) == 0:
            nowFloor = deque(hotel.popleft())
            floor = nowFloor.popleft()
            ho += 1
        else:
            floor = nowFloor.popleft()

    print(floor*100 + ho)