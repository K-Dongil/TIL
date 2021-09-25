import sys
sys.stdin = open("1232_input.txt", "r")

def in_order(root):
    if root:
        left_child = tree[root][1]
        right_child = tree[root][2]
        in_order(left_child)
        in_order(right_child)
        if tree[root][0] == '-':
            tree[root][0] = tree[left_child][0] - tree[right_child][0]
        elif tree[root][0] == '+':
            tree[root][0] = tree[left_child][0] + tree[right_child][0]
        elif tree[root][0] == '*':
            tree[root][0] = tree[left_child][0] * tree[right_child][0]
        elif tree[root][0] == '/':
            tree[root][0] = tree[left_child][0] / tree[right_child][0]
        
tc = 10

for t in range(tc):
    node = int(input())
    tree = [[0]*3 for _ in range(node+1)]

    for i in range(node):
        lst = input().split()

        if len(lst) == 4:
            tree[int(lst[0])][0] = lst[1]
            tree[int(lst[0])][1] = int(lst[2])
            tree[int(lst[0])][2] = int(lst[3])
        else:
            tree[int(lst[0])][0] = int(lst[1])
    
    in_order(1)

    print(f'#{t+1} {int(tree[1][0])}')