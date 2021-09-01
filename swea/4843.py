def getMaxPos(lst):
    MaxP = 0
    N = len(lst)
    for j in range(N):
        if Ai[maxP] < Ai[j]: # maxV < Ai[j]
            #
            maxP = j
    return maxP

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    Ai = list(map(int, input().split()))

    for i in range(N-1):
        if i%2 == 0:
            maxP = getMaxPos(Ai[i:])

            #i번째 위치에 있는 값과 교환
            Ai[maxP], Ai[i] = Ai[i], Ai[maxP]

    else:
        minP = getMinPos(Ai[i:])
        Ai[maxP], Ai[i] = Ai[i], Ai[maxP]

    print('#{}'.format(tc), end = ' ')






def myFunc(tmplst):
    tmplst[1] = 100

lst = [2, 3 ,4 ,5]
myFunc(lst)
print(lst)

lst1 = [2, 3 ,4 ,5]
myFunc(lst1[1:])
print(lst1)