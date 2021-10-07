def partition(l, r):
    p = l
    i = l+1
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