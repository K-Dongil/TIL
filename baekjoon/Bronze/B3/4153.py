def divide(lst):
    if len(lst) == 1:
        return lst
    divideV = len(lst) // 2
    left = lst[divideV:]
    right = lst[:divideV]
    minLeft = divide(left)
    minRight = divide(right)
    res = merge(minLeft, minRight)
    return res

def merge(x, y):
    l = r = 0
    mergeList = []
    while l != len(x) and r != len(y):
        if x[l] < y[r]:
            mergeList.append(x[l])
            l += 1
        elif x[l] > y[r]:
            mergeList.append(y[r])
            r += 1
    
    if l != len(x):
        for num in x[l:]:
            mergeList.append(num)
    elif r != len(y):
        for num in y[r:]:
            mergeList.append(num)
    
    return mergeList

while True:
    lines = list(map(int, input().split()))
    if lines[0] != 0:
        sortLines = divide(lines)
        print('right' if sortLines[0]**2 + sortLines[1]**2 == sortLines[2]**2 else 'wrong')
    else:
        break