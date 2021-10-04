tc = int(input())

for t in range(tc):
    lst = input().split()
    sec = 0
    blue_position = 1
    orange_position = 1
    mission = 1
    blue = []
    orange = []
    b_lst_pos = 0
    o_lst_pos = 0
    button = "N"

    for i in range(len(lst)):
        if lst[i] == "B":
            blue.append(int(lst[i+1]))
        elif lst[i] == "O":
            orange.append(int(lst[i+1]))

    while len(blue) > b_lst_pos or len(orange) > o_lst_pos:
        sec += 1

        if len(blue) <= b_lst_pos:
            pass
        elif lst[mission] == "B" and blue_position == blue[b_lst_pos]:
            b_lst_pos += 1
            button = "Y"
            mission += 2
        elif blue_position < blue[b_lst_pos]:
            blue_position += 1
        elif blue_position > blue[b_lst_pos]:
            blue_position -= 1

        if len(orange) <= o_lst_pos:
            pass
        elif lst[mission] == "O" and orange_position == orange[o_lst_pos]:
            if button == "N":
                o_lst_pos += 1
                mission += 2
        elif orange_position < orange[o_lst_pos]:
            orange_position += 1
        elif orange_position > orange[o_lst_pos]:
            orange_position -= 1

        button = "N"

    print(f'#{t+1} {sec}')
    
# tc = int(input())

# for t in range(tc):
#     lst = input().split()
#     b_sec = 0
#     o_sec = 0
#     result_sec = 0
#     blue_position = 1
#     orange_position = 1
#     blue = []
#     orange = []
#     b_lst_pos = 0
#     o_lst_pos = 0

#     for i in range(len(lst)):
#         if lst[i] == "B":
#             blue.append(int(lst[i+1]))
#         elif lst[i] == "O":
#             orange.append(int(lst[i+1]))

#     while b_lst_pos != len(blue)-1:
#         b_sec += 1
#         if blue_position == blue[b_lst_pos]:
#             b_sec += 1
#             b_lst_pos += 1
#         elif blue_position < blue[b_lst_pos]:
#             blue_position += 1
#         elif blue_position > blue[b_lst_pos]:
#             blue_position -= 1

#     while o_lst_pos != len(orange)-1:
#         o_sec += 1
#         if orange_position == orange[o_lst_pos]:
#             b_sec += 1
#             o_lst_pos += 1
#         elif orange_position < orange[o_lst_pos]:
#             orange_position += 1
#         elif orange_position > orange[o_lst_pos]:
#             orange_position -= 1

#     if b_sec > o_sec:
#         result_sec = b_sec
#     else:
#         result_sec = o_sec

#     print(f'#{t+1} {result_sec}')
    