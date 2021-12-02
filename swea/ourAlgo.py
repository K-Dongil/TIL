tc = int(input())

for t in range(1, tc+1):
    # 입력값
    buySeed = int(input())
    inputList = list(map(int, input().split()))
    lenList = len(inputList)
    startDay = inputList[0]
    canWorkDay = inputList[1]
    canPlantSeed = inputList[-1]
    canSeasons = inputList[2:lenList-1]
    canPlantSeed = inputList[-1]
    seedInfos = [list(map(int, input().split())) for _ in range(buySeed)]

    # 진짜로 심을 수 있는 날짜
    lenCanSeason = len(canSeasons)
    realCanWork = lenCanSeason * 30
    realCanWork -= startDay

    # 진짜로 심을 수 있는 날짜보다 주어진 날짜가 크면 없애기
    idx = 0
    endIdx = 0
    while endIdx == len(seedInfos):
        if seedInfos[idx][1] >= realCanWork:
            seedInfos.pop(idx)
            endIdx += 1
            continue
        idx += 1
        endIdx += 1

    # 주어진 계절에 심을 수 없는 씨앗이면 없애기
    idx = 0
    endIdx = 0
    while endIdx == len(seedInfos):
        result = False
        for season in seedInfos[idx][2:lenList-1]:
            if season in canSeasons:
                result = True
                break
        if result:
            seedInfos.pop(idx)
            endIdx += 1
            continue
        idx += 1
        endIdx += 1

    # 이익 값 계산
    