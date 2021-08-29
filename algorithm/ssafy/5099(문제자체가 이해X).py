tc = int(input())

for t in range(tc):
    N, M = map(int, input().split())
    Ci = [0] +  list(map(int, input().split()))

    q = [0] * N

    newpizza = 1

    while q:
        pizza = q.pop(0)
        Ci[pizza] = Ci[pizza] // 2
        if Ci[pizza] == 0:
            if newpizza <= M:
                q.append(newpizza)
                newpizza += 1
        else:
            q.append(pizza)

    print('#{} {}'.format(t+1, pizza))