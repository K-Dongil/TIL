def pre_order(root):
    global result
    if root != 0:
        left_child_node = int(tree[root][0])
        right_child_node = int(tree[root][1])
        result += 1
        pre_order(left_child_node)
        pre_order(right_child_node)

tc = int(input())

for t in range(tc):
    line, sub_node = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [[0]*2 for _ in range(line+2)]
    result = 0

    for i in range(0, line*2, 2):
        if tree[lst[i]][0] == 0:
            tree[lst[i]][0] = lst[i+1]
        else:
            tree[lst[i]][1] = lst[i+1]
    
    pre_order(sub_node)

    print(f'#{t+1} {result}')