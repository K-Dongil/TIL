# .	평지(전차가 들어갈 수 있다.)
# *	벽돌로 만들어진 벽
# #	강철로 만들어진 벽
# -	물(전차는 들어갈 수 없다.)
# ^	위쪽을 바라보는 전차(아래는 평지이다.)
# v	아래쪽을 바라보는 전차(아래는 평지이다.)
# <	왼쪽을 바라보는 전차(아래는 평지이다.)
# >	오른쪽을 바라보는 전차(아래는 평지이다.)
# U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
# D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
# L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
# R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
# S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.

import sys
sys.stdin = open("1873_input.txt", "r")

def Shoot():
    global row
    global col
    global direction

    if direction == "U":
        for i in range(row-1, -1, -1):
            if map_feature[i][col] == '*':
                map_feature[i][col] = '.'
                break
            elif map_feature[i][col] == '#':
                break
    elif direction == "D":
        for i in range(row+1, len(map_feature)):
            if map_feature[i][col] == '*':
                map_feature[i][col] = '.'
                break
            elif map_feature[i][col] == '#':
                break
    elif direction == "L":
        for i in range(col-1, -1, -1):
            if map_feature[row][i] == '*':
                map_feature[row][i] = '.'
                break
            elif map_feature[row][i] == '#':
                break
    elif direction == "R":
        for i in range(col+1, len(l)):
            if map_feature[row][i] == '*':
                map_feature[row][i] = '.'
                break
            elif map_feature[row][i] == '#':
                break

# 간단하게 바꿔볼 것
def Move(move):
    global row
    global col
    global direction

    if move == 'U':
        if 0 <= row-1 < H and map_feature[row-1][col] == '.':
            map_feature[row][col] = '.'
            row -= 1
        map_feature[row][col] = '^'
        direction = 'U'
    elif move == 'D':
        if 0 <= row+1 < H and map_feature[row+1][col] == '.':
            map_feature[row][col] = '.'
            row += 1
        map_feature[row][col] = 'v'
        direction = 'D'
    elif move == 'L':
        if 0 <= col-1 < W and map_feature[row][col-1] == '.':
            map_feature[row][col] = '.'
            col -= 1
        map_feature[row][col] = '<'
        direction = 'L'
    elif move == 'R':
        if 0 <= col+1 < W and map_feature[row][col+1] == '.':
            map_feature[row][col] = '.'
            col += 1
        map_feature[row][col] = '>'
        direction = 'R'


tc= int(input())

for t in range(1, tc+1):
    H, W = map(int, input().split())
    map_feature = [list(input()) for _ in range(H)]
    user_command = int(input())
    motions = input()
    row = -1
    col = 0
    direction = ''

    for l in map_feature:
        row += 1
        if '^' in l:
            col = l.index('^')
            direction = 'U'
            break
        elif 'v' in l:
            col = l.index('v')
            direction = 'D'
            break
        elif '<' in l:
            col = l.index('<')
            direction = 'L'
            break
        elif '>' in l:
            col = l.index('>')
            direction = 'R'
            break

    for motion in motions:
        if motion == 'S':
            Shoot()
        else:
            Move(motion)
    
    print(f'#{t} ', end='')
    for l in map_feature:
        print(''.join(l))

# =============================================
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# tank = ['^', 'v', '<', '>']

# def find_direc(cy, cx):
#     if game_map[cy][cx] == '^':
#         return 0
#     elif game_map[cy][cx] == 'v':
#         return 1
#     elif game_map[cy][cx] == '<':
#         return 2
#     else:
#         return 3


# def shoot(posy, posx, direction):
#     meet_wall = True
#     while meet_wall:
#         posy += dy[direction]
#         posx += dx[direction]
#         if posy < 0 or posy >= H or posx < 0 or posx >= W:    # 포탄이 맵 밖으로 나가면
#             break
            
#         elif game_map[posy][posx] == '#':
#             meet_wall = False
#         elif game_map[posy][posx] == '*':
#             game_map[posy][posx] = '.'
#             meet_wall = False


# def move(posy, posx, direction):
#     global pos_y, pos_x
#     shape = '^'
#     for i in range(4):
#         if direction == i:
#             posy += dy[i]
#             posx += dx[i]
#             shape = tank[i]
#             break
#     if posy < 0 or posy >= H or posx < 0 or posx >= W:
#         return
#     elif game_map[posy][posx] == '.': # 평지면 탱크위치 옮겨주기
#         game_map[pos_y][pos_x] = '.' # 탱크있던자리에 잔디 깔아주기
#         pos_y += dy[i]
#         pos_x += dx[i]
#         game_map[pos_y][pos_x] = shape



# T = int(input())
# for t in range(1, T+1):
#     H, W = map(int, input().split())
#     game_map = [[] for _ in range(H)]
#     for i in range(H):
#         line = input()
#         for j in line:
#             game_map[i] += j

#     cmd_len = int(input())
#     S = input()
#     cmd_lst = []
#     for i in S:
#         cmd_lst.append(i)

#     pos_y = 0           # 게임 시작시 전차 위치 찾기
#     pos_x = 0
#     for y in range(H):
#         for x in range(W):
#             if game_map[y][x] in tank:
#                 pos_y, pos_x = y, x
#                 break

#     direc = find_direc(pos_y, pos_x)
#     while cmd_lst:
#         cmd = cmd_lst.pop(0)
#         if cmd == 'S':
#             shoot(pos_y, pos_x, direc)
#         else:
#             if cmd == 'U':
#                 game_map[pos_y][pos_x] = '^'
#                 direc = 0
#             elif cmd == 'D':
#                 game_map[pos_y][pos_x] = 'v'
#                 direc = 1
#             elif cmd == 'L':
#                 game_map[pos_y][pos_x] = '<'
#                 direc = 2
#             elif cmd == 'R':
#                 game_map[pos_y][pos_x] = '>'
#                 direc = 3
#             move(pos_y, pos_x, direc)

#     result = [''] * H
#     for i in range(H):
#         for j in range(W):
#             result[i] += game_map[i][j]

#     print(f'#{t}', end = ' ')
#     for i in range(H):
#         print(result[i])