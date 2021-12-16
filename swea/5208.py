def solve(k, remain, cnt):
    global minC

    if minC <= cnt:
        return
    if k== recharge_lst[0]:
        if minC > cnt:
            minC = cnt
        return
    if remain == 0:
        return
    solve(k+1, recharge_lst[k+1], cnt+1)
    solve(k+1, remain-1, cnt)

tc = int(input())

for t in range(1, tc+1):
    recharge_lst = list(map(int, input().split()))+[0]
    minC = 100

    solve(1, recharge_lst[1], 0)
    print(f'#{t} {minC}')