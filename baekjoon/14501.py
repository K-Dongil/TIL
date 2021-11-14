def solve(start):

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
idx = 0
money = 0
while idx < N:
    money += lst[idx][1]
    idx += lst[idx][0]

    if idx == (N-1) and 1 < lst[idx][0]:
        break
print(money)