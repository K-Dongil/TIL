tc = int(input())

for t in range(tc):
    documentNum, position = map(int, input().split())
    queue = list(map(int, input().split()))
    cnt = 0

    while cnt < documentNum:
        maxV = max(queue)
        nowV = queue.pop(0)

        if nowV < maxV:
            queue.append(nowV)
            if 0 < position: 
                position -= 1
            else:
                position = len(queue)-1
        else:
            cnt += 1
            if position == 0:
                break
            position -= 1

    print(cnt)
