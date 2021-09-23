def postorder(root):
    if root != 0:
        left_child_node = int(tree[root][1])
        right_child_node = int(tree[root][2])
        postorder(left_child_node)
        postorder(right_child_node)
        if left_child_node != 0 or right_child_node != 0:
            tree[root][0] = tree[left_child_node][0] + tree[right_child_node][0]

tc = int(input())

for t in range(tc):
    node, leaf, output_num = map(int, input().split())
    tree = [[0]*3 for _ in range(node+1)]
    parent = 1
    child = 2
    
    for i in range(leaf):
        leaf_num, leaf_value = map(int, input().split())
        tree[leaf_num][0] = leaf_value

    while child <= node:
        if child <= node:
            tree[parent][1] = child
            child += 1
        if child <= node:
            tree[parent][2] = child
            child += 1
        parent += 1

    postorder(1)

    print(f'#{t+1} {tree[output_num][0]}')