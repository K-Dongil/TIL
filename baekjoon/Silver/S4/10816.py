def mergeSort(lst):
    if len(lst) == 1:
        return lst
    divideV = len(lst)//2
    leastLeft = mergeSort(lst[:divideV])
    leastRight = mergeSort(lst[divideV:])
    result = merge(leastLeft, leastRight)

    return result

def merge(left, right):
    l = r = 0
    mergeList = []

    while l != len(left) and r != len(right):
        if left[l] <= right[r]:
            mergeList.append(left[l])
            l += 1
        elif right[r] < left[l]:
            mergeList.append(right[r])
            r += 1
    
    if l != len(left):
        for num in left[l:]:
           mergeList.append(num)
    elif r != len(right):
         for num in right[r:]:
           mergeList.append(num)
    
    return mergeList

def binarySearch(v):
    start = 0
    end = cardNum - 1
    middle = end//2
    cnt = 0
    front = 0
    back = 0

    while start <= end:
        middle = (start + end) // 2
        if sortCards[middle] < v:
            start = middle + 1
        elif sortCards[middle] > v:
            end = middle - 1
        else:
            front = middle
            back = middle
            while 0 < front:
                if sortCards[front - 1] != v:
                    break
                else:
                    front -= 1
            while back < cardNum-1:
                if sortCards[back + 1] != v:
                    break
                else:
                    back += 1
            cnt = back - front + 1
            break

    return cnt

cardNum = int(input())
cards = list(map(int, input().split()))
myCardNum = int(input())
myCards = list(map(int, input().split()))
sortCards = sorted(cards)
countRecord = {}
result = ''

for card in myCards:
    if card not in countRecord:
        countRecord[card] = str(binarySearch(card))
    result += countRecord[card] + ' '

print(result)