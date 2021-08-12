def sequential_search(key, lst):
    idx = 0
    N = len(lst)
    # idx를 증가하면서 key를 찾는다
    # key를 찾을 때까지 idx를 증가한다
    while idx < N and key > lst[idx]:
        idx += 1

    if idx < N and key == lst[idx]:
        return idx

    return -1

lst = [2, 4, 7, 9, 11, 19, 23]
print(sequential_search(4, lst)) # 1
print(sequential_search(7, lst)) # 2
print(sequential_search(5, lst)) # -1
print(sequential_search(1, lst)) # -1
print(sequential_search(24, lst)) # -1