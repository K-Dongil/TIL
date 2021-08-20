def rotation_90(lst):
    square_len = len(lst)
    ratation90_lst = [[]*square_len]
    for col in range(len(lst)-1, -1, -1):
        for row in range(len(lst[0])):
            ratation90_lst[col].append([row])
    return ratation90_lst

t = int(input())

for i in range(t):
    square = int(input())
    square_lst = [list(map(int, input().split())) for _ in range(square)]

    print(rotation_90(square_lst))

# def rotation_90(lst):
#     square_len = len(lst)
#     ratation_lst = [[0]*square_len for _ in range(square_len)]
#     for col in range(len(lst)-1, -1, -1):
#         for row in range(len(lst[0])):
#             ratation_lst[col][row] = lst[row][col]