def in_order(root):
    global v
    if root:
        left_child = tree[root][1]
        right_child = tree[root][2]
        in_order(left_child)
        tree[root][0] = v
        v += 1
        in_order(right_child)

tc = int(input())

for t in range(tc):
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    parent = 1
    child = 2
    v = 1

    while child <= N:
        if child <= N:
            tree[parent][1] = child
            child += 1
        if child <= N:
            tree[parent][2] = child
            child += 1
        parent += 1
    
    in_order(1)
    print(f'#{t+1} {tree[1][0]} {tree[N//2][0]}')