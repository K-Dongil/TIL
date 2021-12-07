tc = int(input())

for t in range(1, tc+1):
    wantListenDay = int(input())
    classInfo = list(map(int, input().split()))
    for info in classInfo:
        classInfo.append(info)
        if len(classInfo) == 14:
            break
    weekOpenClass = classInfo.count(1) // 2
    result = []

    for i in range(7): # 어느 요일에서 시작할 것인지 월~일
        if wantListenDay % weekOpenClass == 0:
            minDay = (wantListenDay // weekOpenClass -1) * 7
            remainDay = wantListenDay - (wantListenDay // weekOpenClass -1) * weekOpenClass
        else:
            minDay = (wantListenDay // weekOpenClass) * 7
            remainDay = wantListenDay - (wantListenDay // weekOpenClass) * weekOpenClass
        for j in range(i, i+7): # 일주일
            minDay += 1
            if classInfo[j] == 1:
                remainDay -= 1
            if remainDay == 0:
                result.append(minDay)
                break

    print('#{} {}'.format(t, min(result)))