def partition(l, r):
    x = lst[r]
    i = l - 1
    for i in range(1, r):
        if lst[j] < x:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[r], lst[i+1] = lst[i+1], lst[r]

    return i+1