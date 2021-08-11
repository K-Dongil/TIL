lst = [[1, 2, 3, 4, 5] for i in range(5)] # list Comprehension
sum_lst = []

drow = [-1, 1] # 상하좌우

for row in range(len(lst)):
    for col in range(len(lst[0])):
