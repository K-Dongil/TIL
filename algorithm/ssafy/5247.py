from collections import deque

def solve():
    Q = deque()
    Q.append([(N, 0)])
    while Q:
        curV, cnt = Q.popleft()
        if curV == M:
            return cnt

        t = [curV+1, curV-1, curV*2, curV-10]
        for newV in t:
            if 0 <= newV <= 1000000 and not visited[newV]:
                visited[newV] = True
                Q.append((newV, cnt+1))


TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    visited = [False] * 1000001

    print(f'#{tc} {solve()}')

# def find():
#     q = deque()
#     visited = [False] * 1000001
#     curV = N
#     cnt = 0
#     q.append((curV, cnt))
#     while q:
#         curV, cnt = q.popleft()
#         if curV == M:
#             break
#         else:
#             t = [curV*2, curV-10, curV+1, , curV-1]
#             for newV in t:
#                 if newV > 0 and newV <= 1000000 and not visited[newV]:
#                     visited[nextV] = True
#                     q.append((nextV, cnt+1))


##############
def solve():
    Q = [(N, 0)]
    while Q:
        curV, cnt = Q.pop(0)
        if curV == M:
            return cnt

        t = [curV+1, curV-1, curV*2, curV-10]
        for newV in t:
            if 0 <= newV <= 1000000 and not visited[newV]:
                visited[newV] = True
                Q.append((newV, cnt+1))


TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    visited = [False] * 1000001

    print(f'#{tc} {solve()}')