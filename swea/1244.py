import sys
sys.stdin = open("1244_input.txt", "r")
def selectionS(lst):
    global cnt
    N = len(lst)
    for i in range(N-1):
        maxP = i
        a = 0
        for j in range(i+1, N):
            if lst[maxP] <= lst[j]:
                if lst[maxP] == lst[j]:
                    a += 1
                maxP = j
        if maxP != i:
            lst[maxP], lst[i] = lst[i], lst[maxP]
            cnt -= 1
        if cnt == 0:
            break

tc = int(input())

for t in range(1, tc+1):
    lst, cnt = input().split()
    lst = list(lst)
    cnt = int(cnt)
    selectionS(lst)

    if 0 < cnt:
        cnt = cnt % 2
        if cnt:
            lst[0], lst[1] = lst[1], lst[0]

    print(f'#{t} {"".join(lst)}')


# 교수님 풀이
def solve(k):
    global maxV

    if k==N:
        intV = int(''.join(pan))
        if maxV < intV:
            maxV = intV
        return

    intV = int(''.join(pan)) # 백트래킹
    for i in range(720):
        if state[k][i] == 0:
            state[k][i] == intV
            break
        if state[k][i] == intV: # 여기서 팅겨나가게 해줌
            return

    L = len(pan)
    for i in range(8, L -1):
        for j in range(i + 1, L):
            pan[i], pan[j] = pan[j], pan[i]
            solve(k+1)
            pan[i], pan[j] = pan[j], pan[i]


TC = int(input())

for tc in range(1, TC+1):
    inp, N = input().split()
    pan = list(inp)
    N = int(N)
    state = [[0] * 720 for _ in range(N)] # 6! =720
    maxV = 0
    solve(0)
    print(maxV)
    