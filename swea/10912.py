tc = int(input())

for t in range(tc):
    str = list(input())
    set_str = set(str)
    result = []
    a = ''
    for s in set_str:
        num = str.count(s)
        if num % 2:
            result.append(s)
    result.sort()
    for s in result:
        a += s
    if len(a) == 0:
        a = 'Good'
    print(f'#{t+1} {a}')