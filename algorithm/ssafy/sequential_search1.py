def sequential_search(key, lst):
    idx = 0
    N = len(lst)
    # idx를 증가하면서 key를 찾는다
    # key를 찾을 때까지 idx를 증가한다
    while idx < N and key != lst[idx]:
        idx += 1

    if idx == N: # if문을 while문 안에 넣은다음에 조건문에서 idx < N을 빼주는 방법은 비추천(조건을 먼저 생각했느냐 안 했느냐의 차이)
        return -1
    return idx

lst = [4, 9, 11, 23, 2, 19, 7]
print(sequential_search(2, lst)) # 4
print(sequential_search(8, lst)) # -1
print(sequential_search(4, lst)) # 0
print(sequential_search(7, lst)) # 6