height, width = map(int, input().split())
square = [input() for _ in range(height)]
min_paint =  width * height
first_white_one_line = ''
first_white_two_line = ''
share = width // 2
if square[0][0] == "W":
    if width % 2:
        first_white_one_line = "WB" * share + "W"
        first_white_two_line = "BW" * share + "B"
    else:
        first_white_one_line = "WB" * share
        first_white_two_line = "BW" * share
else:
    if width % 2:
        first_black_one_line = "BW" * share + "B"
        first_black_two_line = "WB" * share + "W"
    else:
        first_black_one_line = "BW" * share
        first_black_two_line = "WB" * share