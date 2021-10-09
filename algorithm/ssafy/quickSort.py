def quickSort(lst, l, r):
    if l < r:
        s = partition(l, r)
        quickSort(lst, l, s-1)
        quickSort(lst, s+1, r)


def partition(l, r):
    p = l
    i = l
    j = r

    while i<j:
        while i<r and lst[i] <= lst[p]:
            i += 1
        while l<j and lst[j] >= lst[p]:
            j -= 1
        if i<j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[p], lst[j] = lst[j], lst[p]
    return j

tc = int(input())

for t in range(1, tc+1):
    N = int(input())
    lst = list(map(int, input().split()))
    quickSort(lst,0, N-1)

    print(f'#{t} {lst[N//2]}')