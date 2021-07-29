import sys
lst = []
for i in range(3):
   lst.append(list(map(int, sys.stdin.readline().split())))
if lst[0][0] == lst[1][0]:
    lst.append([lst[2][0], lst[0][1]+lst[1][1]- lst[2][1]])
elif lst[1][0] == lst[2][0]:
    lst.append([lst[0][0], lst[1][1]+lst[2][1]- lst[0][1]])
else:
    lst.append([lst[1][0], lst[0][1]+lst[2][1]- lst[1][1]])
for i in range(len(lst[3])):
    if i == len(lst[3])-1:
        print(lst[3][i])
    else:
        print(lst[3][i], end=' ')