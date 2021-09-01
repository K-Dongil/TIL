tc = int(input())

for t in range(tc):
    square = int(input())
    height = list(map(int, input().split()))
    max_up = 0
    min_down = 0

    for i in range(square-1):
        if height[i+1] > height[i]:
            up_dif = height[i+1] - height[i]
            if max_up < up_dif:
                max_up = up_dif
        if i < square-2 and height[i+2] < height[i+1]:
            down_dif = height[i+1] - height[i+2]
            if min_down > down_dif:
                min_down = down_dif
    print('#{} {} {}'.format(t+1,max_up, min_down))