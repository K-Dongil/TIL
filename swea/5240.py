def mergesort(lst):
    global count
    if len(lst) == 1:
        return lst
    m = len(lst) // 2
    left = lst[:m]
    right = lst[m:]
    a = mergesort(left) # left가 길이기 1인 list면 a = left가 된다
    b = mergesort(right)
    if a[-1] > b[-1]:
        count += 1
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
        res += left[l:]
    elif r != len(right):
        res += right[r:]
    return res

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    lst = list(map(int, input().split()))
    count = 0

    result = mergesort(lst)
    print(f'#{t} {result[N//2]} {count}')