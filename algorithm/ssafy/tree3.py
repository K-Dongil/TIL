"""
6
2 1 1 3 2 4 3 5 3 6
"""
V = int(input())  # node 개수
edge = list(map(int, input().split()))  # 부모-자식
E = V - 1  # V개의 정점이 있는 트리의 간선 수
par = [0] * (V + 1)

for i in range(E):
    p, c = edge[i * 2], edge[i * 2 + 1]
    par[c] = p  # root를 찾는데 사용


root = 1
while par[root]:
    root += 1
print(root)