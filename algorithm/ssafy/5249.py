tc = int(input())
for tc in range(1, tc+1):
    V, E = map(int, input().split())

    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        a, b, w = map(int, input().split())

        graph[a][b] = graph[b][a] = w

    num = 987654321
    visited = [False] * (V+1)
    distance = [num] * (V+1)

    cur_node = 0
    visited[cur_node] = True
    distance[cur_node] = 0

    connected_edge = 0
    while connected_edge < V:

        for next_node in range(V+1):
            if not visited[next_node] and graph[cur_node][next_node] \
                and graph[cur_node][next_node] < distance[next_node]:
                distance[next_node] = graph[cur_node][next_node]

        min_dist = num
        for next_node in range(V+1):
            if not visited[next_node] and distance[next_node] < min_dist:
                min_dist = distance[next_node]
                cur_node = next_node

        visited[cur_node] = True
        connected_edge += 1

    answer = sum(distance)
    print("#{} {}".format(tc, answer))