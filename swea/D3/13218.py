tc = int(input())

for t in range(1, tc+1):
    student =int(input())
    max_team = student // 3

    print('#{} {}'.format(t, max_team))