tc = int(input())

for t in range(1, tc+1):
    game, voter = map(int, input().split())
    cost_lst = list(map(int, input().split()))
    max_cost = list(map(int, input().split()))
    vote = [0] * game
    position = 0

    for cost in max_cost:
        for i in range(game):
            if cost_lst[i] <= cost:
                vote[i] += 1
                break
    
    for i in range(game):
        if vote[i] == max(vote):
            position = i + 1
            break
    print(f'#{t} {position}')