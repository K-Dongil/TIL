def divide(lst):
    if len(lst) == 1:
        return lst
    divideV = len(lst) // 2
    left = lst[divideV:]
    right = lst[:divideV]
    leftAgain = divide(left)
    rightAgain = divide(right)
    res = merge(leftAgain, rightAgain)
    
    return res

def merge(leftList, rightList):
    l = r = 0
    nowSortList = []
    
    while l != len(leftList) and r != len(rightList):
        if leftList[l] <= rightList[r]:
            nowSortList.append(leftList[l])
            l += 1
        elif rightList[r] < leftList[l]:
            nowSortList.append(rightList[r])
            r += 1
    
    if l != len(leftList):
        for n in leftList[l:]:
            nowSortList.append(n)
    elif r != len(rightList):
        for n in rightList[r:]:
            nowSortList.apend(n)

    return nowSortList

N = int(input())
numList = [int(input()) for _ in range(N)]
sortNum = divide(numList)

for n in sortNum:
    print(n)