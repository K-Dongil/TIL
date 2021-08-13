import copy
import sys

sys.stdin = open('input.txt', 'r')

for tc in range(10):
    tc_num = int(input())
    line_box1 = [list(map(int, input().split())) for _ in range(100)]
    want_start = 0

    for i in range(100):
        col = i
        row = 0
        line_box = copy.deepcopy((line_box1))

        while row < 99:
            if row == 0 and line_box[row][col] == 1 and line_box[row + 1][col] == 1:
                row += 1
                continue
            elif row == 0 and line_box[row][col] == 0:
                break

            if col != 0 and col != 99:
                if line_box[row][col - 1] == 0 and line_box[row + 1][col] == 1 and line_box[row][col + 1] == 0:
                    row += 1
                elif line_box[row][col - 1] == 1:
                    line_box[row][col] = 0
                    col -= 1
                elif line_box[row][col + 1] == 1:
                    line_box[row][col] = 0
                    col += 1
                elif line_box[row + 1][col] == 2:
                    row += 1
            elif col == 0:
                if line_box[row + 1][col] == 1 and line_box[row][col + 1] == 0:
                    row += 1
                elif line_box[row][col + 1] == 1:
                    line_box[row][col] = 0
                    col += 1
                elif line_box[row + 1][col] == 2:
                    row += 1
            elif col == 99:
                if line_box[row][col - 1] == 0 and line_box[row + 1][col] == 1:
                    row += 1
                elif line_box[row][col - 1] == 1:
                    line_box[row][col] = 0
                    col -= 1
                elif line_box[row + 1][col] == 2:
                    row += 1

            if line_box[row][col] == 2:
                want_start = i
                break

        if want_start == 2:
            break
    print('#{} {}'.format(tc_num, want_start))