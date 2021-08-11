def row_sum(lst):
    max_sum = 0
    for row in range(len(lst)):
        sum = 0
        for col in range(len(lst[0])):
            sum += lst[row][col]
        if max_sum < sum:
            max_sum = sum
    return max_sum

def col_sum(lst):
    max_sum = 0
    for col in range(len(lst[0])):
        sum = 0
        for row in range(len(lst)):
            sum += lst[row][col]
        if max_sum < sum:
            max_sum = sum
    return max_sum

# def l_diagonal(lst):
#     sum = 0
#     for row in range(len(lst)):
#         for col in range(len(lst[0])):
#             if row == col:
#                 sum += lst[row][col]
#     return sum

def l_diagonal(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i][i]
    return sum

# def r_diagonal(lst):
#     sum = 0
#     for row in range(len(lst)):
#         for col in range(len(lst[0])):
#             if col == len(lst) -row -1:
#                 sum += lst[row][col]
#     return sum

def r_diagonal(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i][len(lst)-i-1]
    return sum

def max_num(a, b, c, d):
    best = a
    if best < b:
        best = b
    if best < c:
        best = c
    if best < d:
        best = d
    return best

t = 10

for i in range(t):
    tc_num = int(input())
    lst = [list(map(int, input().split())) for h in range(100) ]

    r_sum = row_sum(lst)
    c_sum = col_sum(lst)
    ld_sum = l_diagonal(lst)
    rd_sum = r_diagonal(lst)

    best_sum = max_num(r_sum, c_sum, ld_sum, rd_sum)

    print('#{} {}'.format(tc_num, best_sum))