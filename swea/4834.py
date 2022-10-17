# COUNTS 배열에 있는 가장 큰 값이 있는 위치를 return
def getMaxPost():
    maxV = COUNTS[0]
    maxP = 0

    for i in range(1, len(COUNTS)):
        if maxV < COUNTS[i]: # COUNTS[maxP] < COUNTS[i]
            maxV = COUNTS[i]
            maxP = i

    return maxP

import sys
sys.stdin = open("input4834.txt", "r")

TC = int(input())
for rc in range(1, TC+1):
    N = int(input())
    CARDS = list(map(int, input()))
    #print(N, CARDS) # 4 9 6 7 9

    COUNTS = [0] * 10
    #COUNTS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(N):
        p = CARDS[i]
        COUNTS[p] += 1

    maxpos = getMaxPost() #최대값이 들어 있는 위치를 구해서 return

    print('#{} {} {}'.format())

#==========================
tc = int(input())

for t in range(tc):
    cardNum = int(input())
    inputNums = list(map(int, input()))
    numList = [0] * 11
    maxV = 1
    maxP = numList[1]

    for inputNum in inputNums:
        numList[int(inputNum)] += 1
    
    for i in range(2, 11):
        if maxP <= numList[i]:
            maxV = i
            maxP = numList[i]
	
    print('#{} {} {}'.format(t+1, maxV, maxP))
    