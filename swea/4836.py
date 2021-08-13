def color_paint(king_square, lsts):
    purple = 0
    for lst in lsts:
        if lst[4] == 1:
            for i in range(lst[0], lst[2]+1):
                for j in range(lst[1], lst[3]+1):
                    if king_square[i][j] == 2:
                        purple += 1
                        king_square[i][j] = 3
                    elif king_square[i][j] == 0:
                        king_square[i][j] = 1
        if lst[4] == 2:
            for i in range(lst[0], lst[2]+1):
                for j in range(lst[1], lst[3]+1):
                    if king_square[i][j] == 1:
                        purple += 1
                        king_square[i][j] == 3
                    elif king_square[i][j] == 0:
                        king_square[i][j] == 2
    return purple

t = int(input())

for tc in range(t):
    king_square = [[0]*10 for _ in range(10)]
    vassal_square_num = int(input())
    vassal_square = []

    for i in range(vassal_square_num):
        vassal_square.append(list(map(int, input().split())))
    purple_area = color_paint(king_square, vassal_square)

    print('#{} {}'.format(tc+1, purple_area))