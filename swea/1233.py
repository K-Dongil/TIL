for t in range(1, 11):
    node = int(input())

    tree = [[0]*3 for _ in range(node+1)]
    result = 1

    for i in range(node):
        lst = input().split()

        if len(lst) == 4:
            if lst[1] in ['-', '+', '*', '/']:
                tree[int(lst[0])][0] = lst[1]
            else:
                tree[int(lst[0])][0] = int(lst[1])
                result = 0
            tree[int(lst[0])][1] = int(lst[2])
            tree[int(lst[0])][2] = int(lst[3])
        else:
            if lst[1] in ['-', '+', '*', '/']:
                tree[int(lst[0])][0] = lst[1]
                result = 0
            else:
                tree[int(lst[0])][0] = int(lst[1])

    print(f'#{t} {result}')