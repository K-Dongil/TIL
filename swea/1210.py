import copy
import sys

sys.stdin = open('4843_input.txt', 'r')

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




# #교수님 코드
# import sys

# sys.stdin = open("4843_input.txt", "r")

# TC = 10
# for tc in range(1, TC+1):
#     NO = int(input())

#     BRD = [list(map(int, input().split())) for _ in range(100)]

#     posY = 99
#     for i in range(100):
#         if BRD[posY][i] != 2:
#             continue

#         posX = i
#         while posY >= 0:
#             posY -= 1
#             if posX > 0 and BRD[posY][posX-1] == 1:#좌측에 1이 있으면
#                 while posX > 0 and BRD[posY][posX-1] == 1:
#                     posX -= 1 #왼쪽이 1인동안 좌측으로 이동
#                     #BRD[posY][posX] = 0 # if 와 elif조건을 줬으니 지나간 자리를 0으로 초기화 안 해줘도 된다
#             elif posX <99 and BRD[posY][posX+1] == 1:#우측에 1이 있으면
#                 while posX <99 and BRD[posY][posX+1] == 1:
#                     posX += 1 #오른쪽이 1인동안 우측으로 이동
#                     #BRD[posY][posX] = 0 # if 와 elif조건을 줬으니 지나간 자리를 0으로 초기화 안 해줘도 된다
#         break
#     print('#{} {}'.format(tc, posX))
