def getMaxPos(lst):
    maxV = 0
    N = len(lst)
    for j in range(N):
        if lst[maxV] < lst[j]: # 가장 큰 값의 index값 찾기
            maxV = j
    return maxV

def getMinPos(lst):
    minV = 0
    N = len(lst)
    for j in range(N):
        if lst[minV] > lst[j]: # maxV > Ai[j]
            minV = j
    return minV

tc = int(input())

for t in range(1, tc+1):
    N = int(input())
    numList = list(map(int, input().split()))
    result = ''

    for i in range(10):
        if i%2 == 0:
            maxP = getMaxPos(numList[i:])
            numList[maxP+i], numList[i] = numList[i], numList[maxP+i] # 함수에 보낸 리스트는 i~이므로 return받은 index에 i값을 더해야 한다.
        else:
            minP = getMinPos(numList[i:])
            numList[minP+i], numList[i] = numList[i], numList[minP+i]

    for l in numList[0:10]:
        result += str(l) + ' '

    print('#{} {}'.format(t, result))

def myFunc(tmplst):
    tmplst[1] = 100

lst = [2, 3 ,4 ,5]
myFunc(lst) # callbyreference
print(lst)

lst1 = [2, 3 ,4 ,5]
myFunc(lst1[1:]) # callbyvalue
print(lst1)

#=========================
TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    result_lst = []
    final_result = ''
    for i in range(10): # 특별정렬된 숫자 10개까지 출력
        max_num = num_lst[0]
        min_num = num_lst[0]
        index = 0

        if i % 2 == 0: # 짝수번째일때
            for j in range(len(num_lst)):
                if num_lst[j] >= max_num:
                    max_num = num_lst[j]
                    index = j
        else: # 홀수번째일때
            for j in range(len(num_lst)):
                if num_lst[j] <= min_num:
                    min_num = num_lst[j]
                    index = j

        result_lst.append(num_lst.pop(index))

    for i in result_lst:
        final_result += str(i) + ' '

    print('#{} {}'.format(test_case, final_result))

#==========================================

tc = int(input())

for t in range(1, tc+1):
    N = int(input())
    numList = list(map(int, input().split()))
    sortList = [0] * 10 # 출력결과물이 10개까지만 제한되어 있다.
    ascList = sorted(numList)
    descList = sorted(numList, reverse=True)
    result = ''

    for i in range(10):
        if i % 2 == 0:
            sortList[i] = descList[i//2]
        elif i % 2 != 0:
            sortList[i] = ascList[i//2]
        
    
    for l in sortList:
        result += str(l) + ' '

    print('#{} {}'.format(t, result))
