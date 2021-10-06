def mergesort(lst):
    if len(lst) == 1:
        return lst
    m = len(lst) // 2
    left = lst[:m]
    right = lst[m:]
    a = mergesort(left)
    b = mergesort(right)
    res = merge(a, b)
    return res

def merge(left, right):
    l = r = 0
    res = []
    while l != len(left) and r != len(right) :
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1

    if l != len(left):
        for l in left[l:]:
            res.append(l)
    elif r != len(right):
        for l in right[r:]:
            res.append(l)
    return res

lst1 = [8, 4, 4, 3, 21, 5]
print(mergesort(lst1))