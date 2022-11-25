def divide(lst):
    if len(lst) == 1:
        return lst
    divideNum = len(lst) // 2
    leftDivide = divide(lst[:divideNum])
    rightDivide = divide(lst[divideNum:])
    result  = merge(leftDivide, rightDivide)
    return result

def merge(left, right):
    l = r = 0
    mergeList = []

    while l != len(left) and r != len(right):
        if int(left[l][0]) <= int(right[r][0]):
            mergeList.append(left[l])
            l += 1
        elif int(right[r][0]) < int(left[l][0]):
            mergeList.append(right[r])
            r += 1

    if l != len(left):
        for list in left[l:]:
            mergeList.append(list)
    elif r != len(right):
        for list in right[r:]:
            mergeList.append(list)

    return mergeList

cardNum = int(input())
cardList = list(map(int, input().split()))
myCardNum = int(input())
myCardList = list(map(int, input().split()))
