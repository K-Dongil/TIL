data = [0, 4, 1, 3, 1, 2, 4, 1]

M = 5
N = len(data)
counts = [0] * M
temp = [0] * N
# counts[0] = 1
# counts[4] = 1
# counts[1] = 1
# counts[3] = 1
# counts[1] = 1 + 1


for d in data:
    counts[d] = counts[d] + 1

for i in range(M-1):
    counts[i+1] = counts[i] + counts[i+1]
    #counts[1] = counts[0] + counts[1]
    #counts[2] = counts[1] + counts[2]

for j in range(N-1, -1, -1):
    p = counts[data[j]]
    temp[p] = data[j]
    counts[data[j]] -= 1
    # p1 = data[j] # j=7, i=1
    # p2 = counts[p1] # p2 =4
    # temp[p2] = p1
    # counts[p1] -= 1

print(counts)