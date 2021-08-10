import sys

sys.stdin = open("input4381.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    K, N, M = map(int, input().split())
    CHARGE = list(map(int, input().split()))

    curP = 0
    cnt = 0

    #방법1
    while curP < N:
        nextP = curP + K
        if nextP >= N:
            break

        if nextP not in CHARGE:
            while curP < nextP and nextP not in CHARGE:
                nextP -= 1

            if curP == nextP:
                cnt = 0
                break

        cnt += 1
        curP = next{}


        # if nextP in CHARGE: #충전기가 있나?
        #     cnt += 1
        #     curP = nextP
        # else:
        #     # nexP의 값을 하나씩 빼면서(앞으로 가면서) 충전기가 있는지 확인
        #     while curP < nextP and nextP not in CHARGE:
        #         nextP -= 1
        #
        #     if curP == nextP:
        #         cnt = 0
        #         break
        #     else: # if nextP in CHARGE
        #         cnt += 1
        #         curP = nextP


    #방법2
    CHARGE.insert(0, 0)
    CHARGE.asspend(N)
    lastP = 0
    cnt = 0

    for i in range(len(CHARGE)):
        #충전기 사이의 거리를 확인한다
        if CHARGE[i] - CHARGE[i-1] > K:
            cnt = 0
            break

        #i번째에 있는 충전기에서 충전여부를 결정한다. (i번째에서 직접 결정은 안됨.)
        if CHARGE[i] > lastP + K:
            lastP = CHARGE[i-1]
            cnt += 1

    print('#{} {}'.format(tc, cnt))