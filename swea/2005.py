tc = int(input())

for t in range(tc):
    line = int(input())
    tryangles_lst = []

    for i in range(1, line+1):
        tryangles_lst.append([0]*i)

    print(tryangles_lst)