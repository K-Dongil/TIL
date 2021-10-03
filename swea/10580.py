tc = int(input())

for t in range(tc):
    e_line = int(input())
    height = [list(map(int, input().split())) for _ in range(e_line)]
    cross = 0

    for i in range(len(height)):
        for j in range(i+1, len(height)):
            left, right = height[i][0], height[i][1]
            comparison_left, comparison_right = height[j][0], height[j][1]
            if (left < comparison_left and right > comparison_right) or (left > comparison_left and right < comparison_right):
                cross += 1
    
    print(f'#{t+1} {cross}')