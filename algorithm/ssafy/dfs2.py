# "1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5 ,6, 7 ,3, 7"

lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5 ,6, 6, 7 ,3, 7]
grap = [[0] * 8 for _ in range(8)]
for i in range(0, len(lst), 2):
    s1 = lst[i]
    s2 = lst[i + 1]
    grap[s1][s2] = 1
    grap[s2][s1] = 1

visited = [False] * 8
print(grap)