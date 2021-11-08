tc = int(input())

for t in range(tc):
    damage, level, attack = map(int, input().split())
    total_damage = damage

    for i in range(1, attack):
        total_damage += damage*(1 + i * level / 100)
    
    print(f'#{t+1} {int(total_damage)}')