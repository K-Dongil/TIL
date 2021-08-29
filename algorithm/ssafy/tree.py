# def pre_order(root):
#     if root < N:
#         print(root, tree[root])
#         pre_order(root*2)
#         pre_order(root*2+1)
#
# def pre_order1(root):
#     print(root, tree[root])
#     if root*2 <= N:
#         pre_order(root*2)
#     if root*2 + 1 <= N:
#         pre_order(root*2+1)
#
# N = 10
# tree = [i*100 for i in range(N+1)]
# print(tree)
# pre_order(1)


def pre_order3(root):
    if root != 0:
        print(root, end=' ')
        pre_order3(tree[root][0])
        pre_order3(tree[root][1])

N = 13
inpst = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, inpst.split()))
tree = [[0]*2 for _ in range(N+1)]

for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]

    # 조건에 따라 선택적으로 입력되도록
    if tree[p][0] == 0:
        tree[p][0] = c
    elif tree[p][0] != 0:
        tree[p][1] = c

print(tree)

pre_order3(1)