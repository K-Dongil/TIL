def divide(lst):
    if len(lst) == 1:
        return lst
    divideV = len(lst) // 2
    left = lst[:divideV]
    right = lst[divideV:]
    againLeft = divide(left)
    againRight = divide(right)
    res = merge(againLeft, againRight)
    return res

def merge(left, right):
    l = r = 0
    res = []
    while l != len(left) and r != len(right):
        if right[r] <= left[l]:
            res.append(right[r])
            r += 1
        elif left[l] <=right[r]:
            res.append(left[l])
            l += 1
    
    if l != len(left):
        for n in left[l:]:
            res.append(n)
    elif r != len(right):
        for n in right[r:]:
            res.append(n)
    return res
        
    return 0


N = int(input())
numList = [int(input()) for _ in range(N)]
sortNum = divide(numList)

for num in sortNum:
    print(num)