# lst = [64, 25, 10, 22, 11]
#
# def selectionS(lst):
#     N = len(lst)
#     for i in range(N-1):
#         # i 번째로 작은 값을 찾아서 i 번째 위치에 있는 자료와 교환한다
#         #i에서 시작해서
#         minP = i # minV = lst[i]
#         for j in range(i+1, N):
#             if lst[minP] > lst[j]: # minV > lst[j]
#                 #minV = lst[j]
#                 minP = j
#
#         lst[minP], lst[i] = lst[i], lst[minP]
#
# selectionS(lst)
# print(lst)
#
#
#
# lst = [64, 25, 10, 22, 11]
#
# def selectionS(lst):
#     N = len(lst)
#     for i in range(N-1):
#         # i 번째로 작은 값을 찾아서 i 번째 위치에 있는 자료와 교환한다
#         #i에서 시작해서
#         minV = lst[i]
#         for j in range(i+1, N):
#             if minV > lst[j]: #
#                 #minV = lst[j]
#                 minP = j
#
#         lst[minP], lst[i] = lst[i], lst[minP]
#
# selectionS(lst)
# print(lst)



lst = [64, 25, 10, 22, 11]

def selectionAlgo(lst, k):
    N = len(lst)
    for i in range(k):
        minP = i
        for j in range(i+1, len(lst)):
            if lst[minP] > lst[j]:
                minP = j

        lst[minP], lst[i] = lst[i], lst[minP]
    return lst[k-1]
k_min = selectionAlgo(lst, 2)
print(k_min) # 11