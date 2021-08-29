def in_order(root):
    global result
    if root != 0:
        left_child_node = int(tree[root][1])
        right_child_node = int(tree[root][2])
        in_order(left_child_node)
        result += tree[root][0]
        in_order(right_child_node)

tc = 10

for t in range(tc):
    vertex = int(input()) # 노드의 개수
    tree = [[0]*(3) for _ in range(vertex+1)] # 각 행(노드)에 data, 왼쪽 자식, 오른쪽 자식에 관한 값을 집어 넣을 것이다
    result = ''


    for v in range(vertex):
        info_lst = input().split()
        parent = int(info_lst[0])
        tree[parent][0] = info_lst[1]
        for i in range(2, len(info_lst)):
            if tree[parent][1] == 0:
                tree[parent][1] = info_lst[i]
            elif tree[parent][1] != 0:
                tree[parent][2] = info_lst[i]

    in_order(1) # 문제에서 root의 정점 번호는 반드시 1이라고 가정하였다, 만약 root 정점 번호가 반드시 1이 아닐시 어떻게 구현해야하는지 생각해볼 것
    print('#{} {}'.format(t+1, result))


# #=================================================
# def inorder(root):
#     if root <= N:
#         inorder(root * 2)
#         # print(root)
#         print(tree[root], end='')
#         inorder(root * 2 + 1)
#
#
# for tc in range(10):
#     N = int(input())
#     # N = 8
#     tree = [i for i in range(N + 1)]
#     for i in range(1, N + 1):
#         tree_info = input().split()
#         tree[int(tree_info[0])] = tree_info[1]
#     # print(tree)
#     # print('===중위순회===')
#     print('#{}'.format(tc+1), end=' ')
#     inorder(1)
#     print()