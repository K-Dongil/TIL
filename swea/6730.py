tc = int(input())

for t in range(tc):
    square = int(input())
    height = list(map(int, input().split()))
    max_up = 0
    max_down = 0

    for i in range(square-1):
        if height[i+1] > height[i]:
            up_dif = height[i+1] - height[i]
            if max_up < up_dif:
                max_up = up_dif
        if height[i+1] < height[i]:
            down_dif = height[i] - height[i+1]
            if max_down < down_dif:
                max_down = down_dif
    print('#{} {} {}'.format(t+1,max_up, max_down))