height, width = map(int, input().split())
square = [input() for _ in range(height)]
min_paint =  width * height
first_white_chess = ["WBWBWBWB", "BWBWBWBW"]
first_black_chess = ["BWBWBWBW", "WBWBWBWB"]

go_width = width - 8 + 1
go_height = height - 8 + 1
white_paint_cnt = 0
black_paint_cnt = 0

for w in range(go_width):
    for h in range(go_height):
        white_paint_cnt = 0
        black_paint_cnt = 0
        for i in range(h, h+8):
            line = (i - h) % 2
            for j in range(w, w+8):
                if square[i][j] != first_white_chess[line][j - w]:
                    white_paint_cnt += 1
                if square[i][j] != first_black_chess[line][j - w]:
                    black_paint_cnt += 1
        min_paint = min(min_paint, white_paint_cnt, black_paint_cnt)

print(min_paint)