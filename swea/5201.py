tc = int(input())

for t in range(1, tc+1):
    box, truck = map(int, input().split())
    box_weight = list(map(int, input().split()))
    truck_weight = list(map(int, input().split()))
    can_move = []
    box_weight.sort(reverse=True)
    truck_weight.sort(reverse=True)

    for i in truck_weight:
        for j in box_weight:
            if i >= j:
                box_weight.remove(j)
                can_move.append(j)
                break
    
    result = sum(can_move)
    if not result:
        result = '0'
    print(f'#{t} {result}')