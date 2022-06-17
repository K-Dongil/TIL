def change(idx):
    if idx == 1:
        return None

    if tree[idx] < tree[idx//2]:
        tree[idx], tree[idx//2] = tree[idx//2], tree[idx]
        change(idx//2)

tc = int(input())

for t in range(tc):
    node = int(input())
    v_lst = list(map(int, input().split()))
    tree = [0]*(node+1)
    idx = 2
    sum = 0

    tree[1] = v_lst[0]
    while idx <= node:
        tree[idx] = v_lst[idx-1]
        if tree[idx//2] > tree[idx]:
            change(idx)
        idx += 1

    while node != 1:
        node = node // 2
        sum += tree[node]
    
    print(f'#{t+1} {sum}')

#===================================================
# 재귀X
# tc = int(input())

# for t in range(tc):
#     node = int(input())
#     v_lst = list(map(int, input().split()))
#     tree = [0]*(node+1)
#     idx = 2
#     sum = 0

#     tree[1] = v_lst[0]
#     while idx <= node:
#         tree[idx] = v_lst[idx-1]
#         if tree[idx//2] > tree[idx]:
#             copy_idx = idx
#             while tree[copy_idx//2] > tree[copy_idx]:
#                 tree[copy_idx//2], tree[copy_idx]= tree[copy_idx], tree[copy_idx//2]
#                 copy_idx = copy_idx//2
#         idx += 1

#     while node != 1:
#         node = node // 2
#         sum += tree[node]
    
#     print(f'#{t+1} {sum}')