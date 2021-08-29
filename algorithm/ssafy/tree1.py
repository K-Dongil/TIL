def pre_order(root):
    if root < N:
        print(root, tree[root])
        pre_order(root*2)
        pre_order(root*2+1)

N = 10 # 노드 개수
tree = [i*100 for i in range(N+1)] # len(tree)도 노드의 개수
pre_order(1)